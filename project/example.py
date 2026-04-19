import numpy as np
import pandas as pd
import sys


def main():
    input_dataset = sys.argv[1]
    output_predictions = sys.argv[2]

    df = pd.read_csv(input_dataset)

    # Sanity check -- all the features are there
    columns = set(df.columns.tolist())
    for i in range(1, 24):
        assert f"X{i}" in columns

    # Create a CSV of random predictions
    predictions = pd.DataFrame(
        columns=["PREDICTION"],
        data=np.random.normal(0, 1, size=(df.shape[0], 1)))

    # Save it to the desired file location
    predictions.to_csv(output_predictions, index=False)


if __name__ == "__main__":
    main()
