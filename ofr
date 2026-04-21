import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model(file_path):
    df = pd.read_csv(file_path)

    X = df[['Quantity']]
    y = df['TotalPrice']

    model = LinearRegression()
    model.fit(X, y)

    pickle.dump(model, open("../models/model.pkl", "wb"))
    print("Model trained and saved!")

if __name__ == "__main__":
    train_model("../data/cleaned.csv")
