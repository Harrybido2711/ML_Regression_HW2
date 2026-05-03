import numpy as np
import pandas as pd
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler


def main():
    input_dataset = sys.argv[1]
    output_predictions = sys.argv[2]


    #use the file in course reserve to train train Random Forest model
    feature_cols = [f"X{i}" for i in range(1, 25)]
    train_df = pd.read_csv("data/hw2_project.csv")
    X_train = train_df[feature_cols].values
    y_train = train_df["class"].values
    model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    #use given test from the autograder to test
    test_df = pd.read_csv(input_dataset)
    X_test = test_df[feature_cols].values
    preds = model.predict(X_test).reshape(-1, 1)
    

    # Create a CSV of random predictions
    predictions = pd.DataFrame(columns=["PREDICTION"], data=preds)
    # Save it to the desired file location
    predictions.to_csv(output_predictions, index=False)


if __name__ == "__main__":
    main()
