#!/usr/bin/env python
"""A basic script show casing how to use tweepy.

====================
Tweepy functionality
====================

Over time, the names of various Twitter concepts have evolved, some old names are still used in Tweepy. So keep in mind that, in the context of this article, these equivalences hold:

    - A status is a tweet .
    - A friendship is a follow-follower relationship.
    - A favorite is a like.

Create API object
=================
Objects belonging to the tweepy.API class offer a vast set of methods that
you can use to access almost all Twitter functionality. In the code snippet,
we used update_status() to create a new Tweet.:

    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)

Setting wait_on_rate_limit and wait_on_rate_limit_notify to True makes the
API object print a message and wait if the rate limit is exceeded:

Tweepy Categories
=================
Tweepy’s functionality can be divided into the following groups:

    - OAuth
    - The API class
    - Models
    - Cursors
    - Streams

I've previously set up my OAuth token's so we'll skip those.

API Class
=========
The API methods can be grouped into the following categories:

    - Methods for user timelines
    - Methods for tweets
    - Methods for users
    - Methods for followers
    - Methods for your account
    - Methods for likes
    - Methods for blocking users
    - Methods for searches
    - Methods for trends
    - Methods for streaming


"""
import logging

logging.basicConfig(level=logging.INFO)

import tweepy

from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def run_tweepy():
    """Authenticate to Twitter. """
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        logging.info("Authentication OK")
    except:  # noqa
        logging.error("Error during authentication.")

    # Create a tweet.
    # 07/25/2020: Works!
    api.update_status("Hello tweepy")


if __name__ == "__main__":
    run_tweepy()