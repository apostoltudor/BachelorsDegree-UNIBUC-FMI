import os
import gc
import shutil
import time
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from config import (
    SEED, DEVICE, LR, EPOCHS, BATCH_SIZE, WEIGHT_DECAY,
    LABEL_SMOOTHING, N_FOLDS, EARLY_STOP_PATIENCE,
    TRAIN_CSV, OUTPUT_DIR, BEST_CNN_PATH
)
from models import CustomCNN
from data_loader import get_kfold_splits, get_fold_loaders
from utils import set_seed, plot_confusion_matrix, log_hyperparams


def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()

    avg_loss = running_loss / total
    accuracy = correct / total
    return avg_loss, accuracy


def validate(model, loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    avg_loss = running_loss / total
    accuracy = correct / total
    return avg_loss, accuracy, np.array(all_preds), np.array(all_labels)


def main():
    set_seed(SEED)
    print(f"Device: {DEVICE}")
    print(f"Hiperparametri: LR={LR}, Epochs={EPOCHS}, BS={BATCH_SIZE}, "
          f"WD={WEIGHT_DECAY}, LS={LABEL_SMOOTHING}, Folds={N_FOLDS}")

    train_df = pd.read_csv(TRAIN_CSV)
    splits = get_kfold_splits(train_df)

    best_global_acc = 0.0
    best_global_fold = -1
    fold_accuracies = []

    fold_results = {}

    total_start = time.time()

    for fold_idx in range(N_FOLDS):
        print(f"\n{'=' * 60}")
        print(f"  FOLD {fold_idx + 1}/{N_FOLDS}")
        print(f"{'=' * 60}")

        fold_path = os.path.join(OUTPUT_DIR, f'cnn_fold{fold_idx}.pth')

        if os.path.exists(fold_path):
            print(f"  Checkpoint gasit: {fold_path}")
            print(f"  Skip antrenare — evaluare rapida pe validation set...")

            _, val_loader = get_fold_loaders(train_df, fold_idx, splits)

            model = CustomCNN().to(DEVICE)
            model.load_state_dict(
                torch.load(fold_path, map_location=DEVICE, weights_only=True)
            )
            criterion = nn.CrossEntropyLoss(label_smoothing=LABEL_SMOOTHING)

            _, val_acc, val_preds, val_labels = validate(
                model, val_loader, criterion, DEVICE
            )

            print(f"  Fold {fold_idx + 1} (resumed) — Val acc: {val_acc:.4f}")
            fold_accuracies.append(val_acc)
            fold_results[fold_idx] = (val_preds, val_labels, val_acc)

            if val_acc > best_global_acc:
                best_global_acc = val_acc
                best_global_fold = fold_idx

            del model, criterion, val_loader
            gc.collect()
            if DEVICE.type == 'mps':
                torch.mps.empty_cache()

            continue

        fold_start = time.time()

        train_loader, val_loader = get_fold_loaders(train_df, fold_idx, splits)

        model = CustomCNN().to(DEVICE)
        criterion = nn.CrossEntropyLoss(label_smoothing=LABEL_SMOOTHING)
        optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)

        best_fold_acc = 0.0
        patience_counter = 0
        fold_best_preds = None
        fold_best_labels = None

        for epoch in range(EPOCHS):
            train_loss, train_acc = train_one_epoch(
                model, train_loader, criterion, optimizer, DEVICE
            )
            val_loss, val_acc, val_preds, val_labels = validate(
                model, val_loader, criterion, DEVICE
            )
            scheduler.step()

            if val_acc > best_fold_acc:
                best_fold_acc = val_acc
                patience_counter = 0
                torch.save(model.state_dict(), fold_path)
                fold_best_preds = val_preds.copy()
                fold_best_labels = val_labels.copy()
            else:
                patience_counter += 1

            if (epoch + 1) % 5 == 0 or epoch == 0 or patience_counter >= EARLY_STOP_PATIENCE:
                current_lr = optimizer.param_groups[0]['lr']
                print(f"  Epoch {epoch + 1:3d}/{EPOCHS} | "
                      f"Train L: {train_loss:.4f} A: {train_acc:.4f} | "
                      f"Val L: {val_loss:.4f} A: {val_acc:.4f} | "
                      f"LR: {current_lr:.6f}")

            if patience_counter >= EARLY_STOP_PATIENCE:
                print(f"  Early stopping la epoch {epoch + 1} "
                      f"(fara imbunatatire de {EARLY_STOP_PATIENCE} epoci)")
                break

        fold_time = time.time() - fold_start
        print(f"  Fold {fold_idx + 1} finalizat in {fold_time:.0f}s | "
              f"Best val acc: {best_fold_acc:.4f}")
        fold_accuracies.append(best_fold_acc)
        fold_results[fold_idx] = (fold_best_preds, fold_best_labels, best_fold_acc)

        if best_fold_acc > best_global_acc:
            best_global_acc = best_fold_acc
            best_global_fold = fold_idx

        del model, optimizer, scheduler, criterion
        del train_loader, val_loader
        gc.collect()
        if DEVICE.type == 'mps':
            torch.mps.empty_cache()

    total_time = time.time() - total_start

    mean_acc = np.mean(fold_accuracies)
    std_acc = np.std(fold_accuracies)
    print(f"\n{'=' * 60}")
    print(f"  REZULTATE CROSS-VALIDATION")
    print(f"{'=' * 60}")
    print(f"  Accuracy per fold: {[f'{a:.4f}' for a in fold_accuracies]}")
    print(f"  Mean ± Std: {mean_acc:.4f} ± {std_acc:.4f}")
    print(f"  Best fold: {best_global_fold + 1} (acc: {best_global_acc:.4f})")
    print(f"  Timp total: {total_time:.0f}s ({total_time/60:.1f} min)")

    best_fold_path = os.path.join(OUTPUT_DIR, f'cnn_fold{best_global_fold}.pth')
    shutil.copy2(best_fold_path, BEST_CNN_PATH)
    print(f"  Best model copiat: {BEST_CNN_PATH}")

    print(f"\n  Generare matrice de confuzie...")
    for fold_idx in range(N_FOLDS):
        if fold_idx in fold_results:
            preds, labels, acc = fold_results[fold_idx]
            cm_path = os.path.join(OUTPUT_DIR, f'confusion_matrix_cnn_fold{fold_idx}.png')
            plot_confusion_matrix(
                labels + 1, preds + 1,
                f'CNN Fold {fold_idx + 1} — Acc: {acc:.4f}',
                cm_path
            )

    best_preds, best_labels, _ = fold_results[best_global_fold]
    cm_best_path = os.path.join(OUTPUT_DIR, 'confusion_matrix_cnn_best.png')
    plot_confusion_matrix(
        best_labels + 1, best_preds + 1,
        f'CNN Best Fold {best_global_fold + 1} — Acc: {best_global_acc:.4f}',
        cm_best_path
    )

    hparams = {
        'model': 'CustomCNN',
        'lr': LR,
        'epochs': EPOCHS,
        'batch_size': BATCH_SIZE,
        'weight_decay': WEIGHT_DECAY,
        'label_smoothing': LABEL_SMOOTHING,
        'n_folds': N_FOLDS,
        'early_stop_patience': EARLY_STOP_PATIENCE,
        'optimizer': 'AdamW',
        'scheduler': 'CosineAnnealingLR',
        'fold_accuracies': fold_accuracies,
        'mean_accuracy': float(mean_acc),
        'std_accuracy': float(std_acc),
        'best_fold': best_global_fold,
        'best_accuracy': float(best_global_acc),
        'total_time_seconds': float(total_time)
    }
    log_hyperparams(hparams, os.path.join(OUTPUT_DIR, 'cnn_hyperparams_log.json'))

    print("\nTraining CNN finalizat.")


if __name__ == '__main__':
    main()
