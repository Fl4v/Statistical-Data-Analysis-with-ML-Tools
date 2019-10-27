import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import os

DATASETS = os.path.join('datasets')

# Import the data as a Pandas Dataframe
def data(file_path: str):
    csv_path = os.path.join(DATASETS, file_path)
    return pd.read_csv(csv_path)


# Randomly split your dataset for training and testing of your ml model
def split_train_test_data(data_frame):
    train_set, test_set = train_test_split(data(data_frame), test_size=0.2, random_state=42)
    return train_set, test_set


# Simple function to encode categorical attributes to one-hot vectors
def categorical_attribute_encoder(categorical_attribute: list) -> list:
    encoder = LabelBinarizer()
    one_hot_encoded_attribute = encoder.fit_transform(categorical_attribute)
    return one_hot_encoded_attribute
