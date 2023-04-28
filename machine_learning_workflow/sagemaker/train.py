python
import argparse
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Define argument parser
parser = argparse.ArgumentParser(description='Train a machine learning model.')
parser.add_argument('--input', type=str, default='data/train.csv', help='Input data file path')
parser.add_argument('--output', type=str, default='model.pkl', help='Output model file path')
parser.add_argument('--n_estimators', type=int, default=100, help='Number of trees in the random forest')

# Read arguments
args = parser.parse_args()

# Load data
data = pd.read_csv(args.input)
X = data.drop('target', axis=1)
y = data['target']

# Train model
model = RandomForestClassifier(n_estimators=args.n_estimators)
model.fit(X, y)

# Make predictions and calculate accuracy
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

# Save the model as a binary file
joblib.dump(model, args.output)
