import pandas as pd
import numpy as np
import datetime

#read into python idctionary tweets = {}
#dictionary of user ID's containing list of their tweets
#iterate over list increment counter for each url, div by list length
#MongoDB OR SQLite for database

from collections import defaultdict



def getURLFreq(data):

	d={}
	currentID = ''
	twts = []
	frequencies = {}

	with open(data,'r') as f:
		rows = ( line.split('\t') for line in f ) 

		for row in rows:
			if row[0] == currentID:
				twts.append(row[2]) 
				d[currentID] = twts[:]
			else:
				currentID = row[0]
				del twts[:]
				twts = []
				twts.append(row[2])
				d[currentID] = twts[:]

	for key in d:
		tweetsbyuser = d[key]
		countURLs = 0

		for tweet in tweetsbyuser:
			hasURL = tweet.find("http://")

			if hasURL > 0:
				countURLs += 1

				URLFreq = float(countURLs) / float(len(tweetsbyuser))

				frequencies[key] = URLFreq

	return frequencies

getURLFreq("content_polluters_tweets.txt")

