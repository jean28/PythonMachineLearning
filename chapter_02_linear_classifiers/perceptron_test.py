import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from chapter_02_linear_classifiers.perceptron import Perceptron
from matplotlib.colors import ListedColormap

plot_Iris = False
plot_Perceptron_errors = True

df = pd.read_csv('../data/iris.csv', header=None)

# store the values of the labels for the first 100 training samples
y = df.iloc[0:100, 4].values

# make Iris-setosa -1 and Iris-versicolor into 1
y = np.where(y == 'Iris-setosa', -1, 1)

# store the first (sepal length) and third (petal length) feature columns
# for the first 100 training samples
X = df.iloc[0:100, [0, 2]].values

# plot the data
if plot_Iris:

    # plot setosa (the first 50 values)
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')

    # plot versicolor (50 through 100)
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='o', label='versicolor')

    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend(loc='upper left')
    plt.show()

# Train Perceptron with Data:
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

# plot perceptron errors
if plot_Perceptron_errors:
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.show()


