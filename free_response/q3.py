from src import load_data
from src import LogisticRegression, Perceptron
from src import plt

from free_response.visualize import plot_decision_regions

import sklearn.linear_model
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import PolynomialFeatures


def main():
    # Load data and initialize three models
    X, y, _ = load_data("data/polynomial.csv")
    our_lr = LogisticRegression(max_iter=2000)
    sk_lr = sklearn.linear_model.LogisticRegression(max_iter=2000)
    perceptron = Perceptron(max_iter=2000)

    # Build a 4x3 array of subplots to show results
    fig, axes = plt.subplots(4, 3, figsize=(12, 9),
                             sharex=True, sharey=True)

    # Fit all three models on the untransformed data
    our_lr.fit(X, y)
    our_acc = accuracy_score(y, our_lr.predict(X))
    sk_lr.fit(X, y.flatten())
    sk_acc = accuracy_score(y, sk_lr.predict(X))
    perceptron.fit(X, y)
    p_acc = accuracy_score(y, perceptron.predict(X))

    # Visualize decision regions for untransformed data
    plot_decision_regions(
        X, y, our_lr, axis=axes[0, 0], title=f"Our LR: {our_acc:.3f}")
    plot_decision_regions(
        X, y, sk_lr, axis=axes[0, 1], title=f"sklearn LR: {sk_acc:.3f}")
    plot_decision_regions(
        X, y, perceptron, axis=axes[0, 2], title=f"Perceptron: {p_acc:.3f}",)
    axes[0, 0].set_ylabel("No transformation")

    # For a polynomial transformation of degree 2, 4, and 8
    for i, deg in enumerate([2, 4, 8]):
        Xp = PolynomialFeatures(deg).fit_transform(X)

        # Fit all three models on transformed data
        our_lr.fit(Xp, y)
        our_acc = accuracy_score(y, our_lr.predict(Xp))
        sk_lr.fit(Xp, y.flatten())
        sk_acc = accuracy_score(y, sk_lr.predict(Xp))
        perceptron.fit(Xp, y)
        p_acc = accuracy_score(y, perceptron.predict(Xp))

        # Visualize decision regions for transformed data
        row = i + 1
        plot_decision_regions(
            X, y, our_lr, axis=axes[row, 0], title=f"Our LR: {our_acc:.3f}",
            transform=PolynomialFeatures(deg).fit_transform)
        plot_decision_regions(
            X, y, sk_lr, axis=axes[row, 1], title=f"sklearn LR: {sk_acc:.3f}",
            transform=PolynomialFeatures(deg).fit_transform)
        plot_decision_regions(
            X, y, perceptron, axis=axes[row, 2], title=f"Perceptron: {p_acc:.3f}",
            transform=PolynomialFeatures(deg).fit_transform)
        axes[row, 0].set_ylabel(f"{deg}-degree polynomial")

    # Show figure, save it, and close it
    plt.tight_layout()
    plt.savefig("free_response/q3_polynomial_compare.png")
    plt.show()
    plt.close("all")


if __name__ == "__main__":
    main()
