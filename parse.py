import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from scipy import stats

users = pd.read_csv('users.txt', sep='\t', header=0)
users_features = list(users.columns[:10])

#Function block

def encode(array, data):
	"""encode some data for use in Decision Tree Classifier"""
	le = preprocessing.LabelEncoder()
	le.fit(array[data])
	array[data] = le.transform(array[data])

# def kfold(data):
# 	"""split data into training and test sets"""
# 	kf = KFold(n_splits=10)
# 	for train, test in kf.split(data):
# 		print("%s %s" % (train, test))

# def createTree(array, features, type):
# 	"""create Decision Tree Classifier"""
# 	dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

# 	x = array[features]
# 	y = array[type]

# 	dt.fit(x, y)

# 	return dt

def crossValScore(array, features, type):
	"""Determine the cross validation score for a given array of data"""
	print("Performing cross validation and obtaining scores...")
	dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

	x = array[features]
	y = array[type]

	dt.fit(x, y)

	scores = cross_val_score(dt, x, y, cv=10)

	print("Mean: {:.3f} (std: {:.3f}) (std err: {:.3f})".format(scores.mean(), scores.std(), stats.sem(scores.mean(), axis=None, ddof=0)), end="\n\n")


encode(users, 'createdAt')
encode(users, 'collectedAt')

#kfold(users)

#createTree(users, users_features, "type")

scores = crossValScore(users, users_features, "type")