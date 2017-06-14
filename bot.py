#!/usr/bin/python3

import tweepy
import subprocess
import sys
from time import sleep
from secrets import *

mode = sys.argv[1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(access_token, access_secret)
global api
api = tweepy.API(auth)

def updatecache():
	subprocess.run(["java", "-jar", "ylekov.jar", "update"])

def getpost():
	result = subprocess.run(["java", "-jar", "ylekov.jar", "generate"], stdout=subprocess.PIPE)
	tweet = result.stdout.decode("utf-8").strip()
	return tweet

def testbot():
	print(getpost())

def runbot():
	while True:
		try:
			updatecache()
			api.update_status(getpost())
			sleep(60*60)
		except:
			print("Error: ", sys.exc_info()[0])
			sleep(60)

if mode == "run":
	runbot()
elif mode == "test":
	testbot()
else:
	print("Invoke with 'run' or 'test'")
