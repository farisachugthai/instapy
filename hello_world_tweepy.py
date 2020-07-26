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
Objects belonging to the `tweepy.API` class offer a vast set of methods that
you can use to access almost all Twitter functionality. In the code snippet,
we used ``update_status`` to create a new Tweet.::

Setting ``wait_on_rate_limit`` and ``wait_on_rate_limit_notify`` to True
makes the API object print a message and wait if the rate limit is exceeded:

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
import json
import logging

logging.basicConfig(level=logging.INFO)

import tweepy

from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def run_tweepy():
    """Authenticate to Twitter. """
    try:
        api.verify_credentials()
        logging.info("Authentication OK")
    except:  # noqa
        logging.error("Error during authentication.")

    # Create a tweet.
    # 07/25/2020: Works!
    api.update_status("Hello tweepy")


def read_timeline():
    """Calls ``home_timeline``.

    A tweepy API method used to get the last 20 entries in your timeline.
    """
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")


def get_user(username):
    user = api.get_user(username)
    print("User Details")
    print(user.name)
    print(user.description)
    print(user.location)
    print("Last 20 followers:")
    for follower in user.followers():
        print(follower.name)


def follow_user(username):
    api.create_friendship(username)


def update_profile_description(message):
    api.update_profile(description=message)


def like_most_recent_tweet():
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    api.create_favorite(tweet.id)


def search_twitter(string=None, returned=10):
    """Using these methods, you can search tweets using text, language, and other filters.

    For example, you can try this code to get the 10 most recent public tweets that are in English and contain the word "Python":
    """
    for tweet in api.search(q=string, lang="en", rpp=returned):
        print(f"{tweet.user.name}:{tweet.text}")


def trending_now():
    trends_result = api.trends_place(1)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])


class MyStreamListener(tweepy.StreamListener):
    """
    Streaming allows you to actively watch for tweets that match certain
    criteria in real time. This means that when there aren’t any new tweet
    matching the criteria, then the program will wait until a new tweet is
    created and then process it.

    To use streaming you have to create two objects:

    1. The stream object uses the Twitter API to get tweets that match some criteria. This object is the source of tweets that are then processed by a stream listener.

    2. The stream listener receives tweets from the stream.

    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


def generate_stream():
    """
    We created the stream using tweepy.Stream, passing the authentication
    credentials and our stream listener. To start getting tweets from the
    stream, you have to call the stream’s filter(), passing the criteria to
    use to filter tweets. Then, for each new tweet that matches the criteria,
    the stream object invokes the stream listener’s on_status().
    """
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])


def follow_mentioners():
    """
    Tweepy uses its own model classes to encapsulate the responses from various
    Twitter API methods. This gives you a convenient way to use the results from
    API operations.

    The model classes are:

        - User
        - Status
        - Friendship
        - SearchResults

    Since each tweet object returned by mentions_timeline() belongs to the
    Status class, you can use:

        - favorite() to mark it as Liked
        - user to get its author

    This user attribute, tweet.user, is also an object that belongs to User,
    so you can use follow() to add the tweet’s author to the list of people
    you follow.

    Leveraging Tweepy models enables you to create concise and understandable
    code.
    """

    tweets = api.mentions_timeline()
    for tweet in tweets:
        tweet.favorite()
        tweet.user.follow()


def create_cursor():
    """Cursors handle paginated results automatically.

    Instantiate them by passing a method of the ``api`` object.

    In the example, we used home_timeline() as the source since we wanted tweets
    from the timeline. The Cursor object has an items() method that returns an
    iterable you can use to iterate over the results. You can pass items() the
    number of result items that you want to get.
    """
    for tweet in tweepy.Cursor(api.home_timeline).items(100):
        print(f"{tweet.user.name} said: {tweet.text}")


if __name__ == "__main__":
    run_tweepy()
