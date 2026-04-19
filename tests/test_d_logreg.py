import numpy as np 


def test_logreg():
    from src import LogisticRegression, load_data
    from sklearn.metrics import accuracy_score

    features, targets, _ = load_data('data/parallel-lines.csv')
    max_iter = 1000
    model = LogisticRegression(max_iter=max_iter, learning_rate=1e-1)
    num_iter_to_converge = model.fit(features, targets)
    targets_hat = model.predict(features)
    assert targets_hat.shape == targets.shape

    msg = "your Logistic Regression should fit this parallel-lines perfectly"
    assert accuracy_score(targets, targets_hat) == 1.0, msg

    model = LogisticRegression(max_iter=max_iter, learning_rate=0.0)
    num_iter_to_converge = model.fit(features, targets)
    targets_hat = model.predict(features)

    msg = "with learning rate = 0, LogisticRegression can't learn"
    assert accuracy_score(targets, targets_hat) < 1.0, msg


def test_polynomial_logreg():
    from src import LogisticRegression, load_data
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import PolynomialFeatures

    features, targets, _ = load_data('data/circles.csv')
    max_iter = 1000
    logreg = LogisticRegression(max_iter=max_iter)
    num_iter = logreg.fit(features, targets)
    targets_hat = logreg.predict(features)

    msg = "linear logreg can't fit circles"
    assert accuracy_score(targets, targets_hat) < 1.0, msg

    msg = "after polynomial transform, should fit perfectly"
    poly_features = PolynomialFeatures(2).fit_transform(features)
    num_iter = logreg.fit(poly_features, targets)
    targets_hat = logreg.predict(poly_features)
    assert accuracy_score(targets, targets_hat) == 1.0, msg
