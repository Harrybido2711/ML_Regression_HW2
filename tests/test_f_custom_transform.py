import numpy as np
import src.random
from src.logistic_regression import LogisticRegression
from sklearn.metrics import accuracy_score


def get_message(msg):
    reminder = "Remember! `test_custom_transform` isn't worth many points!"
    if np.random.random() < 0.05:
        return reminder
    else:
        return msg


def test_custom_transform():
    from src import load_data
    from src import custom_transform

    X, y, _ = load_data("data/spiral.csv")

    new_X = custom_transform(X)
    msg = "Only use at most three features"
    assert new_X.shape[1] <= 3, get_message(msg)

    model = LogisticRegression()
    model.fit(new_X, y)
    preds = model.predict(new_X).reshape(-1, 1)
    acc = accuracy_score(y, preds)
    msg = f"Custom transform at {100 * acc:.1f}% accuracy, want 90%."
    assert acc >= 0.9, get_message(msg)

    # Don't just memorize the order of the data!
    src.random.rng.seed()
    for _ in range(4):
        shuffle = np.argsort(src.random.rand(X.shape[0]))
        X1 = X[shuffle, :]
        y1 = y[shuffle]
        model = LogisticRegression()
        new_X1 = custom_transform(X1)
        model.fit(new_X1, y1)
        preds = model.predict(new_X).reshape(-1, 1)
        acc2 = accuracy_score(y, preds)
        diff = np.abs(acc - acc2)
        msg = f"Shuffling the data shouldn't change your accuracy: {diff:.2f}"
        assert diff < 0.05, get_message(msg)

    # Don't just memorize the location of every point!
    src.random.rng.seed()
    for _ in range(4):
        X2 = X + src.random.normal(0, 0.01, size=X.shape)
        model = LogisticRegression()
        new_X2 = custom_transform(X2)
        model.fit(new_X2, y)
        preds = model.predict(new_X2).reshape(-1, 1)
        acc3 = accuracy_score(y, preds)
        msg = "A tiny bit of random noise shouldn't hurt"
        assert np.abs(acc - acc3) < 0.1, get_message(msg)
