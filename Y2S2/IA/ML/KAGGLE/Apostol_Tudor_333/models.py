import torch
import torch.nn as nn
from config import NUM_CLASSES


class ResidualBlock(nn.Module):

    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = self.relu(out)
        return out


class CustomCNN(nn.Module):

    def __init__(self, in_channels=3, num_classes=NUM_CLASSES):
        super().__init__()

        self.block1 = nn.Sequential(
            ResidualBlock(in_channels, 64),
            nn.MaxPool2d(2),
            nn.Dropout2d(0.25)
        )

        self.block2 = nn.Sequential(
            ResidualBlock(64, 128),
            nn.MaxPool2d(2),
            nn.Dropout2d(0.25)
        )

        self.block3 = nn.Sequential(
            ResidualBlock(128, 256),
            nn.MaxPool2d(2),
            nn.Dropout2d(0.25)
        )

        self.block4 = nn.Sequential(
            ResidualBlock(256, 512),
            nn.AdaptiveAvgPool2d(1)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.5),
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        x = self.block4(x)
        x = self.classifier(x)
        return x

