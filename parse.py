import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from scipy import stats
from getURLFreq import getURLFreq

#Function block

def encode(array, data):
	"""encode some data for use in Decision Tree Classifier"""
	le = preprocessing.LabelEncoder()
	le.fit(array[data])
	array[data] = le.transform(array[data])

def crossValScore(array, features, type):
	"""Determine the cross validation score for a given array of data"""
	print("Performing cross validation and obtaining scores...")
	dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

	#del users_features[8] #Discard "type" column as it causes the system to "cheat"

	x = array[features]
	y = array[type]

	dt.fit(x, y)

	scores = cross_val_score(dt, x, y, cv=10)

	print("Mean: {:.3f} (std: {:.3f}) (std err: {:.3f})".format(scores.mean(), scores.std(), stats.sem(scores.mean(), axis=None, ddof=0)))

def assignType(data, type):
	if type == 'bot':
		data['type'] = 1
	if type == 'human':
		data['type'] = 0


botData = pd.read_csv('content_polluters.txt', sep='\t', header=0)
humanData = pd.read_csv('legitimate_users.txt', sep='\t', header=0)


assignType(botData, 'bot')
assignType(humanData, 'human')

frames = [botData, humanData]

userData = pd.concat(frames)

encode(userData, 'createdAt')
encode(userData, 'collectedAt')

#botFreq = getURLFreq("content_polluters_tweets.txt")
#humanFreq = getURLFreq("legitimate_users_tweets.txt")

users_features = list(userData.columns[3:7])

scores = crossValScore(userData, users_features, "type")
