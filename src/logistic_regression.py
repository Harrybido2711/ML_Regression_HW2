import numpy as np
import warnings


def sigmoid(z):
    """
    Helper function to compute the logistic function (sigmoid) for you.
    You shouldn't need to edit this.

    See: https://en.wikipedia.org/wiki/Logistic_function
    """
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", "overflow encountered in exp")
        return 1 / (1 + np.exp(-z))


class LogisticRegression():
    def __init__(self, learning_rate=1e-1, max_iter=200):
        """
        A logistic regression classifier. This binary classifier learns a
        linear boundary that separates input space into two, such that points
        on one side of the line are one class and points on the other side are
        the other class.

        Read the `logistic_regression.pdf` handout in the base folder of your
        repository before trying to implement this! 

        Args:
            max_iter (int): the algorithm stops after this many iterations if
                it has not converged.

            learning_rate (float): how large of a gradient step to take at each
                update.

        """
        self.max_iter = max_iter
        self.learning_rate = learning_rate

    def fit(self, X, y):
        """
        Fit the model to the data. You should not have to modify this
        function -- all your work should go in `update_weights` and `predict`.

        Note: self.add_intercept is called to add an intercept to the features

        Args:
            X (np.ndarray): a NxK array containing N examples each with K features.
            y (np.ndarray): a Nx1 array containing binary targets.
        Returns:
            n_iters: the number of iterations the model took to converge,
                or self.max_iter
        """
        X2 = self.add_intercept(X)
        self.weights = np.zeros((X2.shape[1], 1))

        for n_iters in range(1, 1 + self.max_iter):
            stop = self.update_weights(X2, y)
            if stop:
                break

        return n_iters

    def add_intercept(self, X):
        """
        Helper function to add a column of 1's to your features
        """
        return np.concatenate([np.ones([X.shape[0], 1]), X], axis=1)

    def update_weights(self, X, y):
        """
        Perform one iteration of gradient descent for LogisticRegression
        Note: don't forget to use `self.learning_rate` to scale the amount of
            the update.

        Pseudocode:
            for each example in X
                compute the gradient of binary cross entropy loss update the weights to better classify the data
            return whether the model has converged

        Args:
            X: the Nx(K+1) matrix of features, including an intercept
            y: the Nx1 array of targets

        Returns:
            stop: Boolean indicating whether the model has converged
            (Do not return the weights; update those in-place)
        """
        N = X.shape[0] #the number of features

        # h(X) = sigmoid(X @ w), formula (4) in pdf
        h = sigmoid(X @ self.weights)

        #calculate the gradient, formula (10) in pdf
        gradient = X.T @ (h - y) / N

        #update the weights
        self.weights = self.weights - self.learning_rate * gradient

        # return true if the gradient is small enough
        return np.linalg.norm(gradient) < 1e-4



    def predict(self, X):
        """
        Given features, a 2D numpy array, use the trained model to predict
        target classes. Call this after calling fit.

        Note: Keep the `self.add_intercept` code to ensure you include the
            intercept

        Args:
            X (np.ndarray): 2D array containing real-valued inputs.
        Returns:
            predictions (np.ndarray): Output of trained model on features,
                with predictions as {0, 1} labels.
        """
        
        X = self.add_intercept(X)
        h = sigmoid(X @ self.weights)
        # if any entry >= 0.5, then return true (1), vice versa
        return (h >= 0.5).astype(int)

        
    
