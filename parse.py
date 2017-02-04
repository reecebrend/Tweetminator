import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import KFold

users = pd.read_csv('users.txt', sep='\t', header=0)
users_features = list(users.columns[:10])

#Function block

def encode(array, data):
	"""encode some data for use in Decision Tree Classifier"""
	le = preprocessing.LabelEncoder()
	le.fit(array[data])
	array[data] = le.transform(array[data])

def kfold(data):
	"""split data into training and test sets"""
	kf = KFold(n_splits=10)
	for train, test in kf.split(data):
		print("%s %s" % (train, test))

def createTree(array, features, type):
	"""create Decision Tree Classifier"""
	dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

	x = array[features]
	y = array[type]

	dt.fit(x, y)


encode(users, 'createdAt')
encode(users, 'collectedAt')

kfold(users)

createTree(users, users_features, "type")