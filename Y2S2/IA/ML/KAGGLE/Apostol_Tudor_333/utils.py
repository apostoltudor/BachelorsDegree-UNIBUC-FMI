import os
import json
import random
import numpy as np
import torch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def plot_confusion_matrix(y_true, y_pred, title, save_path):
    class_names = ['1', '2', '3', '4', '5']
    cm = confusion_matrix(y_true, y_pred, labels=[1, 2, 3, 4, 5])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)

    fig, ax = plt.subplots(figsize=(8, 6))
    disp.plot(ax=ax, cmap='Blues', values_format='d')
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('Predicted', fontsize=11)
    ax.set_ylabel('True', fontsize=11)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close(fig)
    print(f"  Confusion matrix salvata: {save_path}")


def log_hyperparams(params_dict, filepath):
    logs = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append(params_dict)
    with open(filepath, 'w') as f:
        json.dump(logs, f, indent=2, default=str)
    print(f"  Hyperparams logged: {filepath}")
