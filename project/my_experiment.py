import numpy as np
import pandas as pd
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from src.regression import PolynomialRegression
from src.metrics import mean_squared_error


def main():
    #read the data file
    df = pd.read_csv("data/hw2_project.csv")
    # Sanity check -- all the features are there
    columns = set(df.columns.tolist())
    for i in range(1, 25):
        assert f"X{i}" in columns

    feature_cols = [f"X{i}" for i in range(1, 25)]
    X = df[feature_cols].values
    y = df["class"].values.ravel() #change into 1D array

    # 1. PolynomialRegression in different degree
    for degree in [1, 2, 3]:
        rmse_list = []
        # cross validation
        N = len(X)
        fold_size = N // 5
        for k in range(5):
            val_idx = range(k * fold_size, (k + 1) * fold_size)
            train_idx = list(range(0, k * fold_size)) + list(range((k + 1) * fold_size, N))
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]
            model = PolynomialRegression(degree=degree)
            model.fit(X_train, y_train.reshape(-1, 1))
            preds = model.predict(X_val)
            rmse = np.sqrt(np.mean((preds - y_val.reshape(-1, 1))**2))
            rmse_list.append(rmse)
        print(f"PolynomialRegression degree={degree} RMSE: {np.mean(rmse_list):.4f}")

    
    #2. train Random Forest model
    model_rf = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
    scores = cross_val_score(model_rf, X, y, cv=5, scoring='neg_root_mean_squared_error')
    print(f"RandomForest RMSE: {-scores.mean():.4f}")

if __name__ == "__main__":
    main()