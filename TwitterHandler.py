#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '361916496-MTO3esqpLApk5SZrDHhbeaWrt3PBIc6TnuhGb0ue'
access_token_secret = 'CcAr9Jt57Zue5Rvewa61hBu6OcVJYOCypqWxKVEFjmC9O'
consumer_key = 'fiXKnxgDrptoaDIwPWaWFOwLO'
consumer_secret = 'RAzTaXyb2sW6gZJ1eRk9yxeSfoRnk5ywYnalV9VA5zWD3mWnNU'

authid = tweepy.OAuthHandler(consumer_key, consumer_secret)
authid.set_access_token(access_token, access_token_secret)
api = tweepy.API(authid)

# define user to get tweets for. accepts input from user
user = api.get_user(input("Please enter the twitter username: "))

# Display basic details for twitter user name
print (" ")
print ("Basic information for", user.name)
print ("Screen Name:", user.screen_name)
print ("Name: ", user.name)
print user.Description

timeline = api.user_timeline(screen_name=user.screen_name, include_rts=False, count=10)

print("got timeline")

for tweet in timeline:
    print ("Text:", tweet.text)