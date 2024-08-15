"""
Train and test a model based on the data stored in data-mappings.json, to be used in main.py.
"""

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# Hyperparameters
LEARNING_RATE = 0.001
EPOCHS = 10
BATCH_SIZE = 64

# Model parameters
INPUT_CHANNELS = None
NUM_CLASSES = None
KERNEL_SIZE = None
DEVICE = "cpu"

class DesignPredictorModel(nn.Module):
    def __init__(self):
        super(DesignPredictorModel, self).__init__()
        

    def forward(self, x):
        return x


transform = transforms.Compose([
    transforms.CenterCrop((500, 500)),
    transforms.Resize((200, 200)),
    transforms.ToTensor(),
])

train_dataset = None
test_dataset = None

train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE, shuffle=False)

model = DesignPredictorModel().to(DEVICE)

loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

for epoch in range(EPOCHS):
    for batch_index, (data, target) in enumerate(train_loader):
        data, target = data.to(DEVICE), target.to(DEVICE)

        outputs = model(data)
        loss = criterion(outputs, target)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()