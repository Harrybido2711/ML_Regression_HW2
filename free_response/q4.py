import argparse
import os

import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures

from src import load_data, plt

from free_response.visualize import plot_decision_regions
from free_response.visualize import compute_bounds


def main(n_folds=9, show=True, save=True):
    # Load data and initialize three models
    X, y, _ = load_data("data/polynomial.csv")
    logreg = LogisticRegression(max_iter=2000)
    n_col = 3
    n_row = int(np.ceil(n_folds / n_col))
    fig, axes = plt.subplots(
          n_row, n_col,
          figsize=(3 * n_col, 3 * n_row),
          sharex=True, sharey=True)
    axes = np.atleast_2d(axes)

    bounds = compute_bounds(X)
    deg = 2
    transform = lambda x: polynomial_transform(x, deg)

    for i, indices in enumerate(KFold(n_folds).split(X, y)):
        # grab the training and test data
        (train_index, test_index) = indices
        X_train = X[train_index]
        y_train = y[train_index]
        X_test = X[test_index]
        y_test = y[test_index]

        # transform the training and test data
        Xp_train = PolynomialFeatures(deg).fit_transform(X_train)
        Xp_test = PolynomialFeatures(deg).fit_transform(X_test)

        # fit the model
        logreg.fit(Xp_train, y_train.flatten())
        preds = logreg.predict(Xp_test)
        prec = precision_score(y_test, preds, zero_division=np.nan)
        rec = recall_score(y_test, preds, zero_division=np.nan)

        # index into your plots
        row = i // 3
        col = i % 3
        title = f"{i}: {prec:.3f} prec, {rec:.3f} recall"
        plot_decision_regions(
            X_test, y_test, logreg, bounds=bounds, axis=axes[row, col],
            title=title, transform=PolynomialFeatures(deg).fit_transform)
              
        axes[row, 0].set_ylabel(f"{deg}-degree polynomial")

    # Show figure, save it, and close it
    plt.suptitle(f"cv{n_folds}.png")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    if save:
        fn = os.path.join("free_response", f"q4_cv{n_folds}.png")
        print(f"Saving plot to {fn}")
        plt.savefig(fn)
    if show:
        plt.show()
    plt.close("all")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--noshow", action='store_true')
    parser.add_argument("--nosave", action='store_true')
    args = parser.parse_args()

    print((
        "WARNING!\n"
        "The default behavior of this script is to generate three PNGs"
        " sequentially, showing each onscreen and then saving them to file."
        " You must *close* the image display for the next to show up.\n"
        "Rerun the script with --noshow to suppress showing them onscreen.\n"
        "Rerun the script with --nosave to suppress saving them to file."
    ))

    main(3, show=not args.noshow, save=not args.nosave)
    main(6, show=not args.noshow, save=not args.nosave)
    main(9, show=not args.noshow, save=not args.nosave)
