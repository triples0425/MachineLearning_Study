#------------ chapter 1. ---------------------
#from sklearn import datasets

#house_prices = datasets.load_boston()

#print(house_prices.data)

#print(house_prices.target)
#------------ chapter 1. end ----------------

#---------------logisticRegression----------------
#import numpy as np
#import matplotlib.pyplot as plt

#from sklearn import linear_model

#from utilities import visualize_classifier

#X = np.array([[3.1, 7.2], [4, 6.7], [2.9, 8], [5.1,4.5], [6, 5], [5.6, 5], [3.3, 0.4], [3.9, 0.9], [2.8, 1], [0.5, 3.4], [1, 4], [0.6, 4.9]])
#y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])

#classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

#classifier.fit(X, y)

#visualize_classifier(classifier, X, y)
#---------------logisticRegression----------------

import numpy as np
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation

from utilities import visualize_classifier

