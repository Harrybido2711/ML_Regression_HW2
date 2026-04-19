import datetime
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src import load_data, plt
from src import custom_transform

from free_response.visualize import plot_decision_regions


def visualize_spiral():
    """
    Helper function to help visualize the spiral dataset
    """
    X, y, _ = load_data("data/spiral.csv")
    axis = plt.subplot()
    axis.scatter(X[:, 0], X[:, 1], c=y)
    plt.show()
    plt.close("all")


def visualize_transform():
    """
    Helper function to help visualize your data transformation
    """

    X, y, _ = load_data("data/spiral.csv")
    new_X = custom_transform(X)
    fig = plt.figure()

    # If 2D, plot 2D
    if new_X.shape[1] == 2:
        axis = plt.axes()
        axis.scatter(new_X[:, 0], new_X[:, 1], c=y)
    else:
        # Else plot 3D
        assert new_X.shape[1] == 3
        axis = fig.add_subplot(projection='3d')
        y1 = (y == 1).flatten()
        axis.scatter(new_X[y1, 0], new_X[y1, 1], new_X[y1, 2], c='r', depthshade=False)
        y0 = (y == 0).flatten()
        axis.scatter(new_X[y0, 0], new_X[y0, 1], new_X[y0, 2], marker='*', c='b', depthshade=False)

    plt.show()
    plt.close("all")


if __name__ == "__main__":
    """
    You don't have to use this code if you don't want, but it may
    help you visualize the spiral and your transformations thereof.
    """
    print("Showing plot 1 of 2")
    visualize_spiral()
    print("Showing plot 2 of 2")
    visualize_transform()
