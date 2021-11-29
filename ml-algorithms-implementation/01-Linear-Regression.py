import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
from sklearn import datasets
from sklearn.model_selection import train_test_split
from tqdm import tqdm
warnings.filterwarnings("ignore")


class LinearRegression(object):
    def __init__(self, learning_rate=0.01, iterations=100):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.cost_history = None
        self.bias = None

    def fit(self, X, y):
        n_samples,n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.cost_history = np.zeros(self.iterations)
        self.bias = 0

        # gradient descent algorithm
        for i in tqdm(range(self.iterations)):
            y_pred = np.dot(X, self.weights) + self.bias
            cost = (1 / 2 * n_samples)*np.sum((y_pred - y) ** 2)
            self.cost_history[i] = cost

            gradient_weights = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            gradient_bias = (1 / n_samples) * np.sum((y_pred- y))

            # update parameters
            self.weights -= self.learning_rate * gradient_weights
            self.bias -= self.learning_rate * gradient_bias 

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


def mean_squared_error(y_true,y_pred):
    return np.mean(y_true - y_pred) ** 2


if __name__ == '__main__':
    X, y = datasets.make_regression(n_samples = 10000, n_features = 4, random_state=0)
    X_train ,X_test,y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

    lr = LinearRegression(learning_rate = 0.0001,iterations = 1000)
    lr.fit(X_train,y_train)
    y_preds = lr.predict(X_test)

    print(f"mean squared error : {mean_squared_error(y_test, y_preds)}")

