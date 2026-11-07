
from pandas import DataFrame
import numpy

from numpy.typing import NDArray


def sigmoïd(z: NDArray[numpy.float64]) -> NDArray[numpy.float64]:
    return 1. / (1. + numpy.exp(-z))

def train_binary(
    X: DataFrame,
    y_binary: NDArray[numpy.float64],
    learning_rate: float=0.1,
    epochs:int=1000
):

    # m: number of train sample (students)
    # n: number of features
    m, n = X.shape

    weights = numpy.zeros(n)
    bias = 0

    for i in range(epochs):
        predictions = probability(X, weights, bias)

        # Gradient descend
        delta_teta = (1/m) * numpy.dot(X.T, predictions - y_binary)
        delta_bias = (1/m) * numpy.sum(predictions - y_binary)

        weights -= learning_rate * delta_teta
        bias -= learning_rate * delta_bias

    return weights, bias

def probability(
    X: DataFrame,
    weights:NDArray[numpy.float64],
    bias: float
) -> NDArray[numpy.float64]:

    # Prediction
    z = numpy.dot(X, weights) + bias
    # Probability
    return sigmoïd(z)

def train_ova(
    X: DataFrame,
    y: NDArray[numpy.int64],
    learning_rate: float = 0.1,
    epochs: int = 1000
) -> tuple[NDArray[numpy.float64], NDArray[numpy.float64], NDArray[numpy.int64]]:


    classes = numpy.unique(y)
    all_weights = []
    all_biases = []
    for c in classes:
        y_binary = (y == c).astype(numpy.int64)
        weights, bias = train_binary(X, y_binary, learning_rate, epochs)

        all_weights.append(weights)
        all_biases.append(bias)

    return numpy.array(all_weights), numpy.array(all_biases), classes


def predict(
    X:DataFrame,
    weights:NDArray[numpy.float64],
    biases:NDArray[numpy.float64],
    classes:NDArray[numpy.int64],
) -> numpy.ndarray:
    # X: all students
    # weights: weights of the four models
    # biases: biases of the four models

    probabilities = sigmoïd(
        numpy.dot(X, weights.T) + biases
    )
    print(probabilities)
    predictions = numpy.argmax(probabilities, axis=1)

    return classes[predictions]
