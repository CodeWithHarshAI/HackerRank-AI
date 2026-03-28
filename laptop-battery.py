import pandas as pd
from sklearn import linear_model

# Load dataset
dataset = pd.read_csv('trainingdata.txt', header=None)

# Remove capped values
dataset = dataset[dataset.iloc[:,1] < 8]

# Split X and Y
X = dataset.iloc[:,0].to_numpy().reshape(-1,1)
Y = dataset.iloc[:,1].to_numpy()

# Train model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Input
timeCharged = float(input().strip())

# Predict
result = model.predict([[timeCharged]])

# Cap at 8
if result[0] > 8:
    print(8.0)
else:
    print(round(result[0], 2))
