import os
import sys
import numpy as np
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from sklearn.model_selection import StratifiedKFold
from config import (
    TRAIN_DIR, TEST_DIR, TRAIN_CSV, TEST_CSV,
    BATCH_SIZE, NUM_WORKERS, N_FOLDS, SEED, HIST_BINS
)


class SignalDataset(Dataset):

    def __init__(self, dataframe, img_dir, transform=None, is_test=False):
        self.df = dataframe.reset_index(drop=True)
        self.img_dir = img_dir
        self.transform = transform
        self.is_test = is_test

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        img_name = self.df.iloc[idx]['id']
        img_path = os.path.join(self.img_dir, img_name)

        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        if self.is_test:
            return image, img_name

        label = int(self.df.iloc[idx]['label']) - 1
        return image, label


train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.RandomRotation(degrees=10),
    transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 1.0)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

val_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


def get_kfold_splits(train_df, n_folds=N_FOLDS, seed=SEED):
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    return list(skf.split(train_df['id'], train_df['label']))


def get_fold_loaders(train_df, fold_idx, splits, batch_size=BATCH_SIZE):
    train_indices, val_indices = splits[fold_idx]

    train_subset = train_df.iloc[train_indices]
    val_subset = train_df.iloc[val_indices]

    train_dataset = SignalDataset(train_subset, TRAIN_DIR, transform=train_transform)
    val_dataset = SignalDataset(val_subset, TRAIN_DIR, transform=val_transform)

    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True,
        num_workers=NUM_WORKERS, pin_memory=False
    )
    val_loader = DataLoader(
        val_dataset, batch_size=batch_size, shuffle=False,
        num_workers=NUM_WORKERS, pin_memory=False
    )

    return train_loader, val_loader


def get_test_loader(test_df, batch_size=BATCH_SIZE):
    test_dataset = SignalDataset(test_df, TEST_DIR, transform=val_transform, is_test=True)
    return DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False,
        num_workers=NUM_WORKERS, pin_memory=False
    )


def extract_classic_features(df, img_dir):
    n = len(df)
    features = []

    for idx in range(n):
        img_name = df.iloc[idx]['id']
        img_path = os.path.join(img_dir, img_name)
        img = Image.open(img_path).convert('RGB')
        arr = np.array(img, dtype=np.float32) / 255.0

        feat = []

        for c in range(3):
            hist, _ = np.histogram(arr[:, :, c], bins=HIST_BINS, range=(0.0, 1.0))
            hist = hist.astype(np.float32)
            hist_sum = hist.sum()
            if hist_sum > 0:
                hist = hist / hist_sum
            feat.extend(hist.tolist())

        for c in range(3):
            channel = arr[:, :, c].flatten()
            ch_mean = float(channel.mean())
            ch_std = float(channel.std()) + 1e-8
            ch_skew = float(np.mean(((channel - ch_mean) / ch_std) ** 3))
            feat.extend([ch_mean, ch_std, ch_skew])

        gray = arr.mean(axis=2)
        feat.extend([
            float(gray.mean()),
            float(gray.std()),
            float(gray.min()),
            float(gray.max())
        ])

        features.append(feat)

        if (idx + 1) % 2000 == 0 or idx == n - 1:
            print(f"  Feature extraction: {idx + 1}/{n}", flush=True)

    return np.array(features, dtype=np.float32)
