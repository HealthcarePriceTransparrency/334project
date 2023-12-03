from sklearn import tree
from sklearn.tree import plot_tree, DecisionTreeRegressor
import numpy as np
import pandas as pd
import time
from sklearn import metrics
import matplotlib.pyplot as plt

start = time.time()
# reading already split data
xtrain = pd.read_csv("xTrain.csv")
xtest = pd.read_csv("xTest.csv")
ytrain = pd.read_csv("yTrain.csv")
ytest = pd.read_csv("yTest.csv")

xtrain = xtrain.to_numpy()
xtest = xtest.to_numpy()
ytrain = ytrain.to_numpy()
ytest = ytest.to_numpy()
yraveltrain = ytrain.ravel()
ytrain = np.array(yraveltrain).astype(int)
yraveltest = ytest.ravel()
ytest = np.array(yraveltest).astype(int)

tree = DecisionTreeRegressor()
tree.fit(xtrain, ytrain)
testPred = tree.predict(xtest)
trainPred = tree.predict(xtrain)
testAcc = metrics.accuracy_score(ytest, testPred)
trainAcc = metrics.accuracy_score(ytrain, trainPred)
testAuc = metrics.roc_auc_score(ytest, testPred)
trainAuc = metrics.roc_auc_score(ytrain, trainPred)

# graph of decision tree created
plot_tree(tree, feature_names= ("npi_number","payer","city","state"), filled=True, rounded=True)
timeElapsed = time.time() - start

print("Time Elapsed: ", timeElapsed)
print("Test Accuracy: ", testAcc)
print("Train Accuracy: ", trainAcc)
print("Test AUC: ", testAuc)
print("Train AUC: ", trainAuc)

plt.show()
