from sklearn import tree
from sklearn.tree import plot_tree, DecisionTreeRegressor
import numpy as np
import pandas as pd
import time
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


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

tree = DecisionTreeRegressor(criterion = "friedman_mse", min_samples_leaf=2, max_depth = 100)
tree.fit(xtrain, ytrain)
testPred = tree.predict(xtest)
trainPred = tree.predict(xtrain)
trainr2 = r2_score(trainPred, ytrain)
testr2 = r2_score(testPred, ytest)

print("Train R2: ", trainr2)
print("Test R2: ", testr2)
importances = tree.feature_importances_
indices = np.argsort(importances)

# graph of feature importance
plt.title('Feature Importance')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), ("npi_number","payer","city","state"))
plt.xlabel('Relative Importance')
plt.show()

# graph of decision tree created
plot_tree(tree, feature_names= ("npi_number","payer","city","state"), filled=True, rounded=True)
timeElapsed = time.time() - start

print("Time Elapsed: ", timeElapsed)

plt.show()

print("Test AUC: ", testAuc)
print("Train AUC: ", trainAuc)

plt.show()
