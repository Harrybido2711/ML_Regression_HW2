import numpy as np


def custom_transform(data):
    """
    Transform the `spiral.csv` data such that it can be more easily classified.

    To pass test_custom_transform, your transformation should create at most
    three features and should allow a LogisticRegression model to achieve at
    least 90% accuracy.

    You can use free_response.custom_transform.visualize_spiral() to visualize
    the spiral as we give it to you, and
    free_response.custom_transform.visualize_transform() to visualize the 2D or
    3D data transformation you implement here.

    NOTE: this test case can require significant trial and error. It is only
    worth about half a point towards your final grade. Please do not spend
    several hours on it, unless you really want to.

    Args:
        data: an array of shape (N, 2) from the `spiral.csv` dataset.

    Returns:
        A transformed data matrix that is (more) easily classified.
            this can be either an array of shape (N, 2) or (N, 3).
    """

    x1 = data[:, 0]
    x2 = data[:, 1]
    raise NotImplementedError


    
