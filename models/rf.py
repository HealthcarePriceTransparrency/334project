import time
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import metrics
from sklearn import tree
from sklearn.tree import plot_tree, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import StratifiedKFold, KFold, cross_val_score, cross_validate

# rf function takes in n_estimators, max_depth, and min_samples_leaf as parameters
def rf(n, m, l):
    start = time.time()
    xtrain = pd.read_csv("xTrain.csv")
    xtest = pd.read_csv("xTest.csv")
    ytrain = pd.read_csv("yTrain.csv")
    ytest = pd.read_csv("yTest.csv")
    xtrain = xtrain.to_numpy()
    xtest = xtest.to_numpy()
    # returns 1d arrays of ytrain and ytest so that it can be used in r2_score
    ytrain = ytrain.to_numpy().flatten()
    ytest = ytest.to_numpy().flatten()

    # create random forest regressor with specified parameters
    forest = RandomForestRegressor(n_estimators=n, max_depth=m, min_samples_leaf=l)

    forest.fit(xtrain, ytrain)
    testPred = forest.predict(xtest)
    trainPred = forest.predict(xtrain)

    trainr2 = r2_score(trainPred, ytrain)
    testr2 = r2_score(testPred, ytest)
    timeElapsed = time.time() - start

    print("Time Elapsed: ", timeElapsed)
    # prints out parameters and r2 scores
    print("n_estimators: ", n)
    print("max_depth: ", m)
    print("min_samples_leaf: ", l)
    print("Train R2: ", trainr2)
    print("Test R2: ", testr2)

def main():
    n = 100
    m = 450
    l = 1
    k = 5

    # reads and formats data
    xTrain = pd.read_csv("xTrain.csv")
    yTrain = pd.read_csv("yTrain.csv")
    yTrain = yTrain.to_numpy().flatten()
    xTest = pd.read_csv("xTest.csv")
    xTest = xTest.to_numpy()
    yTest = pd.read_csv("yTest.csv")
    yTest = yTest.to_numpy().flatten()

    randForest = RandomForestRegressor(n_estimators=n, max_depth=m, min_samples_leaf=l)
    # cross validation with 5 folds
    cv_results = cross_validate(randForest, xTrain, yTrain, cv=k, scoring='r2')
    print('\n fit_time \n', cv_results['fit_time'])
    print('\n score_time \n', cv_results['score_time'])
    print('\n test_score \n', cv_results['test_score'])
    return 0;

if __name__ == "__main__":
    main()
