import os
import torch

SEED = 42

NUM_CLASSES = 5
IMG_HEIGHT = 128
IMG_WIDTH = 55
IN_CHANNELS = 3

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(_SCRIPT_DIR, '..', 'signal-object-detection')
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
TEST_DIR = os.path.join(DATA_DIR, 'test')
TRAIN_CSV = os.path.join(DATA_DIR, 'train.csv')
TEST_CSV = os.path.join(DATA_DIR, 'test.csv')

if torch.backends.mps.is_available():
    DEVICE = torch.device('mps')
elif torch.cuda.is_available():
    DEVICE = torch.device('cuda')
else:
    DEVICE = torch.device('cpu')

LR = 1e-3
EPOCHS = 60
BATCH_SIZE = 32
NUM_WORKERS = 0
N_FOLDS = 5
WEIGHT_DECAY = 1e-4
LABEL_SMOOTHING = 0.05
EARLY_STOP_PATIENCE = 15

SVM_C_VALUES = [0.1, 1, 10, 100]
SVM_GAMMA_VALUES = ['scale', 'auto']
SVM_KERNEL = 'rbf'
HIST_BINS = 32

OUTPUT_DIR = _SCRIPT_DIR
BEST_CNN_PATH = os.path.join(OUTPUT_DIR, 'best_cnn_model.pth')
SVM_MODEL_PATH = os.path.join(OUTPUT_DIR, 'best_svm_model.joblib')
SCALER_PATH = os.path.join(OUTPUT_DIR, 'svm_scaler.joblib')
