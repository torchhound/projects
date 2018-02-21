import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib
import matplotlib.pyplot as plt

np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise = 0.2)
plt.scatter(X[:,0], X[:,1], s = 40, c = y, cmap = plt.cm.Spectral)

#logistic regression classifier training
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)

def plotDecisionBoundary(pred_func):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap = plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.Spectral)

#plot the decision boundary
plotDecisionBoundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")


