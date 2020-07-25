#!/usr/bin/env python
import tweepy

from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
# Objects belonging to the tweepy.API class offer a vast set of methods that
# you can use to access almost all Twitter functionality. In the code snippet,
# we used update_status() to create a new Tweet.
api = tweepy.API(auth)

# Create a tweet.
# 07/25/2020: Works!
api.update_status("Hello tweepy")
