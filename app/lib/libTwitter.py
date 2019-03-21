# GetOldTweets for Python 3
from app.scripts.GetOldTweets.got3.manager.TweetCriteria import TweetCriteria
from app.scripts.GetOldTweets.got3.manager.TweetManager import TweetManager


class libTwitter:
    def __init__(self):
        pass

    @staticmethod
    def fetch_tweets(i_items, s_query=None, s_since=None, s_until=None, s_lang=None):
        o_tweet_criteria = TweetCriteria().setMaxTweets(i_items)

        if (s_since is None or s_until is None) and (s_since != s_until):
            print("No value on one of the following: since and until parameter.")
        else:
            if s_query is not None:
                o_tweet_criteria = o_tweet_criteria.setQuerySearch(s_query)
            if s_since is not None and s_until is not None:
                o_tweet_criteria = o_tweet_criteria.setSince(s_since).setUntil(s_until)
            if s_lang is not None:
                o_tweet_criteria = o_tweet_criteria.setLang(s_lang)
            o_tweet_criteria.near = "Calabarzon, Republic of the Philippines"

        a_tweets = TweetManager.getTweets(o_tweet_criteria)
        a_tweets = libTwitter.__build_tweet_array(a_tweets)
        return a_tweets

    @staticmethod
    def __build_tweet_array(a_tweets):
        a_new_tweets = []
        for a_tweet in a_tweets:
            a_temp_tweet = {
                "message": a_tweet.text,
                "origin": "twitter",
                "date": a_tweet.date.strftime("%Y-%m-%d"),
            }
            a_new_tweets.append(a_temp_tweet)

        return a_new_tweets
