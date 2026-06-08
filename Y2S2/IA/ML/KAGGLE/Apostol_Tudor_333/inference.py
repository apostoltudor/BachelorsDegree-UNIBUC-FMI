import os
import argparse
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import joblib

from config import (
    DEVICE, NUM_CLASSES, N_FOLDS,
    TEST_CSV, TEST_DIR, OUTPUT_DIR,
    BEST_CNN_PATH, SVM_MODEL_PATH, SCALER_PATH
)
from models import CustomCNN
from data_loader import get_test_loader, extract_classic_features


def inference_cnn_ensemble(test_df):
    test_loader = get_test_loader(test_df)

    models = []
    for fold_idx in range(N_FOLDS):
        fold_path = os.path.join(OUTPUT_DIR, f'cnn_fold{fold_idx}.pth')
        if not os.path.exists(fold_path):
            print(f"  Warning: cnn_fold{fold_idx}.pth nu exista, skip")
            continue
        model = CustomCNN().to(DEVICE)
        model.load_state_dict(torch.load(fold_path, map_location=DEVICE, weights_only=True))
        model.eval()
        models.append(model)

    if not models:
        if os.path.exists(BEST_CNN_PATH):
            print("  Folosesc best_cnn_model.pth (un singur model)")
            model = CustomCNN().to(DEVICE)
            model.load_state_dict(torch.load(BEST_CNN_PATH, map_location=DEVICE, weights_only=True))
            model.eval()
            models.append(model)
        else:
            raise FileNotFoundError("Niciun model CNN gasit. Ruleaza train_cnn.py mai intai.")

    n_models = len(models)

    tta_transforms = [
        lambda x: x,
        lambda x: torch.flip(x, dims=[3]),  # Flip orizontal
        lambda x: torch.flip(x, dims=[2]),  # Flip vertical
    ]
    print(f"  Ensemble: {n_models} modele x {len(tta_transforms)} TTA variante = {n_models * len(tta_transforms)} predictii/imagine")

    all_ids = []
    all_preds = []

    with torch.no_grad():
        for images, img_names in test_loader:
            images = images.to(DEVICE)

            avg_probs = torch.zeros(images.size(0), NUM_CLASSES, device=DEVICE)
            for tta_fn in tta_transforms:
                augmented = tta_fn(images)
                for model in models:
                    logits = model(augmented)
                    probs = F.softmax(logits, dim=1)
                    avg_probs += probs
            avg_probs /= (n_models * len(tta_transforms))

            _, predicted = avg_probs.max(1)
            predicted = predicted.cpu().numpy() + 1

            all_ids.extend(list(img_names))
            all_preds.extend(predicted.tolist())

    return all_ids, all_preds


def inference_svm(test_df):
    if not os.path.exists(SVM_MODEL_PATH):
        raise FileNotFoundError(f"SVM model nu exista: {SVM_MODEL_PATH}. "
                                f"Ruleaza train_classic.py mai intai.")

    svm = joblib.load(SVM_MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    print("  Extragere features pt. test set...")
    features = extract_classic_features(test_df, TEST_DIR)
    features_scaled = scaler.transform(features)

    preds = svm.predict(features_scaled)
    ids = test_df['id'].values.tolist()

    return ids, preds.tolist()


def save_submission(ids, preds, filename):
    sub = pd.DataFrame({'id': ids, 'label': preds})
    out_path = os.path.join(OUTPUT_DIR, filename)
    sub.to_csv(out_path, index=False)
    print(f"  Submission salvat: {out_path} ({len(sub)} samples)")
    unique, counts = np.unique(preds, return_counts=True)
    dist = dict(zip(unique, counts))
    print(f"  Distributie predictii: {dist}")


def main():
    parser = argparse.ArgumentParser(
        description='Generare submission Kaggle pt. signal classification'
    )
    parser.add_argument(
        '--model', type=str, default='cnn',
        choices=['cnn', 'svm', 'both'],
        help='Model pt. inferenta: cnn (ensemble), svm, sau both'
    )
    args = parser.parse_args()

    test_df = pd.read_csv(TEST_CSV)
    print(f"Test set: {len(test_df)} imagini")

    if args.model in ('cnn', 'both'):
        print("\n--- CNN Ensemble Inference ---")
        ids, preds = inference_cnn_ensemble(test_df)
        save_submission(ids, preds, 'submission_cnn.csv')

    if args.model in ('svm', 'both'):
        print("\n--- SVM Inference ---")
        ids, preds = inference_svm(test_df)
        save_submission(ids, preds, 'submission_svm.csv')

    print("\nInferenta finalizata.")


if __name__ == '__main__':
    main()
