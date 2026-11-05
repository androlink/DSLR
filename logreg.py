
import numpy


def predict(X: numpy.ndarray, theta: numpy.ndarray, bias: float) -> float:
    return numpy.dot(X, theta) + bias

def sigmoïd(z: numpy.ndarray) -> numpy.ndarray:
    return 1 / (1 + numpy.exp(-z))

def train_binary(X: numpy.ndarray,
    y_binary: numpy.ndarray,
    learning_rate: float=0.1,
    epochs:int=1000):

    # n: number of train sample (students)
    # m: number of features
    m, n = X.shape

    weights = numpy.zeros(n)
    bias = 0

    for i in range(epochs):

        predictions = probability(X, weights, bias)

        # Gradient
        delta_teta = (1/m) * numpy.dot(X.T, predictions - y_binary)
        delta_bias = (1/m) * numpy.sum(predictions - y_binary)

        weights -= learning_rate * delta_teta
        bias -= learning_rate * delta_bias

    return weights, bias

def probability(X: numpy.ndarray, weights:numpy.ndarray, bias: float) -> float:

    # Prediction
    z = numpy.dot(X, weights) + bias
    # Probability
    return sigmoïd(z)
