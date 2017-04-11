import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from scipy import stats
from getURLFreq import getURLFreq
import csv
import sys
from twitterHandler import getUserAttributes
import cgi

#Function block

def encode(array, data):
	"""encode some data for use in Decision Tree Classifier"""
	le = preprocessing.LabelEncoder()
	le.fit(array[data])
	array[data] = le.transform(array[data])

def crossValScore(array, features, type):
	"""Determine the cross validation score for a given array of data"""
	print("Performing cross validation and obtaining scores...")
	

	#del users_features[8] #Discard "type" column as it causes the system to "cheat"

	x = array[features]
	y = array[type]

	dt.fit(x, y)

	scores = cross_val_score(dt, x, y, cv=10)

	print("Mean Accuracy: {:.3f} (std: {:.3f}) (std err: {:.3f})".format(scores.mean(), scores.std(), stats.sem(scores.mean(), axis=None, ddof=0)))


def assignType(data, type):
	if type == 'bot':
		data['type'] = 1
	if type == 'human':
		data['type'] = 0



#def assignURLFreqs(humanFreqs ,botFreqs):
#	botData['URLfreq'] = 0
#	humanData['URLfreq'] = 0
#	for i in xrange(0, len(humanFreqs)):
#		humanData['URLfreq'][i] = humanFreqs[i]
#	for i in xrange(0, len(botFreqs)):
#		botData['URLfreq'][i] = botFreqs[i]

dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

def predictUser(username):

	print("Importing CSV files into Pandas Dataframes...\n")
	botData = pd.read_csv('content_polluters.txt', sep='\t', header=0)
	humanData = pd.read_csv('legitimate_users.txt', sep='\t', header=0)

	print("Assigning types to data for Decision Tree Model...\n")
	assignType(botData, 'bot')
	assignType(humanData, 'human')

	print("Combining human and bot data into single dataframe...\n")
	frames = [botData, humanData]
	userData = pd.concat(frames)

	print("Adding URL Frequencies to data frame...")
	userData['URLFreq'] = 0
	userData['URLFreq'][0] = "URLFreq"

	with open("URLFreqs.tsv") as input:
		for line in csv.reader(input, delimiter='\t'):
			freqs = line

	freqSeries = pd.Series(freqs)
	userData['URLFreq'] = freqSeries

	print("Encoding dates into int form via label encoder...\n")
	encode(userData, 'createdAt')
	encode(userData, 'collectedAt')
	
	users_features = ['descLen', 'nameLen', 'numFollowers', 'numFollowings','numTweets', 'URLFreq']

	scores = crossValScore(userData, users_features, "type")

	userAttributes = getUserAttributes(username)

	predict = dt.predict_proba(userAttributes, users_features)

	print("raw results: ", predict)
	print("chance of being human: ", predict[0][0])
	return {'username': username, 'predict': predict[0][0]}



