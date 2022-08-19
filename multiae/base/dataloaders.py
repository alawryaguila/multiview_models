import random
import numpy as np
import pandas as pd
import pytorch_lightning as pl

from torchvision import transforms
from torch.utils.data import DataLoader
from .datasets import MVDataset

class MultiviewDataModule(pl.LightningDataModule):

    def __init__(
            self,
            batch_size,
            is_validate,
            train_size,
            data,
            labels
        ):

        super().__init__()
        self.batch_size = batch_size
        self.is_validate = is_validate
        self.train_size = train_size
        self.data = data    # TODO: do not save?
        self.labels = labels # TODO: do not save?

        if not isinstance(self.batch_size, int):
            self.batch_size = self.data[0].shape[0]

    def setup(self, stage):
        if self.labels is not None:
            self.labels = self.process_labels(self.labels)
        if self.is_validate:
            train_data, test_data, train_labels, test_labels = self.train_test_split()
            self.train_dataset = MVDataset(data=train_data, labels=train_labels)
            self.test_dataset = MVDataset(data=test_data, labels=test_labels)
        else:
            self.train_dataset = MVDataset(data=self.data, labels=self.labels) 
            self.test_dataset = None

    def train_test_split(self):

        N = self.data[0].shape[0]
        train_idx = list(random.sample(range(N), int(N * self.train_size)))
        test_idx = np.setdiff1d(list(range(N)), train_idx)

        train_data = []
        test_data = []
        for dt in self.data:
            train_data.append(dt[train_idx, :])
            test_data.append(dt[test_idx, :])

        train_labels = None
        test_labels = None
        if self.labels is not None:
            train_labels = self.labels[train_idx]
            test_labels = self.labels[test_idx]

        return train_data, test_data, train_labels, test_labels

    def process_labels(self, labels):
        if isinstance(labels, pd.core.series.Series):
            return self.labels.values.reshape(-1)
        elif isinstance(labels, np.ndarray):
            return self.labels.reshape(-1)
        elif isinstance(labels, list):
            return np.array(self.labels)

    def train_dataloader(self):
        # TODO: other settings? like num_workers
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=False, num_workers=0) #use default num_workers for now, problem in windows! 

    def val_dataloader(self):
        if self.is_validate:
            return DataLoader(
                self.test_dataset, batch_size=self.batch_size, shuffle=False, num_workers=0)
        return None
