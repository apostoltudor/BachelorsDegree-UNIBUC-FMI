import os
import time
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
import joblib

from config import (
    SEED, N_FOLDS, TRAIN_CSV, TRAIN_DIR,
    SVM_C_VALUES, SVM_GAMMA_VALUES, SVM_KERNEL, HIST_BINS,
    OUTPUT_DIR, SVM_MODEL_PATH, SCALER_PATH
)
from data_loader import extract_classic_features
from utils import set_seed, plot_confusion_matrix, log_hyperparams


def main():
    set_seed(SEED)
    start_time = time.time()

    print("Incarcare date de training...")
    train_df = pd.read_csv(TRAIN_CSV)
    labels = train_df['label'].values

    print("Extragere features (histograme culoare + statistici)...")
    features = extract_classic_features(train_df, TRAIN_DIR)
    print(f"Feature matrix: {features.shape} "
          f"({features.shape[1]} features per imagine)")

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    folds = list(skf.split(features_scaled, labels))

    best_acc = 0.0
    best_params = {}
    all_results = []

    print(f"\nGrid Search: C={SVM_C_VALUES}, gamma={SVM_GAMMA_VALUES}, "
          f"kernel={SVM_KERNEL}")
    print(f"{'C':>8s} | {'gamma':>6s} | {'Mean Acc':>9s} | {'Std':>7s}")
    print("-" * 40)

    for C in SVM_C_VALUES:
        for gamma in SVM_GAMMA_VALUES:
            fold_accs = []
            fold_preds_list = []
            fold_labels_list = []

            for fold_idx, (train_idx, val_idx) in enumerate(folds):
                X_train = features_scaled[train_idx]
                X_val = features_scaled[val_idx]
                y_train = labels[train_idx]
                y_val = labels[val_idx]

                svm = SVC(C=C, gamma=gamma, kernel=SVM_KERNEL, random_state=SEED)
                svm.fit(X_train, y_train)
                acc = svm.score(X_val, y_val)
                fold_accs.append(acc)

                if fold_idx == N_FOLDS - 1:
                    fold_preds_list = svm.predict(X_val).tolist()
                    fold_labels_list = y_val.tolist()

            mean_acc = np.mean(fold_accs)
            std_acc = np.std(fold_accs)

            result = {
                'C': C,
                'gamma': gamma,
                'kernel': SVM_KERNEL,
                'mean_accuracy': float(mean_acc),
                'std_accuracy': float(std_acc),
                'fold_accuracies': [float(a) for a in fold_accs]
            }
            all_results.append(result)

            print(f"{C:8.1f} | {str(gamma):>6s} | {mean_acc:9.4f} | {std_acc:7.4f}")

            if mean_acc > best_acc:
                best_acc = mean_acc
                best_params = {'C': C, 'gamma': gamma}
                best_val_preds = fold_preds_list
                best_val_labels = fold_labels_list

    print(f"\nBest: C={best_params['C']}, gamma={best_params['gamma']}, "
          f"acc={best_acc:.4f}")

    print("\nAntrenare SVM final pe intreg dataset-ul...")
    final_svm = SVC(
        C=best_params['C'], gamma=best_params['gamma'],
        kernel=SVM_KERNEL, random_state=SEED, probability=True
    )
    final_svm.fit(features_scaled, labels)

    joblib.dump(final_svm, SVM_MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"SVM model salvat: {SVM_MODEL_PATH}")
    print(f"Scaler salvat: {SCALER_PATH}")

    best_train_idx, best_val_idx = folds[-1]
    svm_eval = SVC(
        C=best_params['C'], gamma=best_params['gamma'],
        kernel=SVM_KERNEL, random_state=SEED
    )
    svm_eval.fit(features_scaled[best_train_idx], labels[best_train_idx])
    val_preds = svm_eval.predict(features_scaled[best_val_idx])
    val_acc = svm_eval.score(features_scaled[best_val_idx], labels[best_val_idx])

    cm_path = os.path.join(OUTPUT_DIR, 'confusion_matrix_svm.png')
    plot_confusion_matrix(
        labels[best_val_idx], val_preds,
        f'SVM (C={best_params["C"]}, gamma={best_params["gamma"]}) — '
        f'Acc: {val_acc:.4f}',
        cm_path
    )

    total_time = time.time() - start_time

    log_hyperparams({
        'model': 'SVM',
        'kernel': SVM_KERNEL,
        'hist_bins': HIST_BINS,
        'n_features': int(features.shape[1]),
        'best_C': best_params['C'],
        'best_gamma': best_params['gamma'],
        'best_cv_accuracy': float(best_acc),
        'all_results': all_results,
        'total_time_seconds': float(total_time)
    }, os.path.join(OUTPUT_DIR, 'svm_hyperparams_log.json'))

    print(f"\nTraining SVM finalizat in {total_time:.0f}s ({total_time/60:.1f} min).")


if __name__ == '__main__':
    main()
