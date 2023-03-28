import tweepy
import config
import re

class twitterConnection:

    def __init__(self):
        self.consumer_key = config.api_key
        self.consumer_secret = config.api_secrets
        self.access_token = config.access_token
        self.access_token_secret = config.access_secret
        self.bearer_token = config.bearer_token
        try:
            self.api = tweepy.Client(bearer_token=self.bearer_token)
        except:
            print("Error: Authentication Failed")

    
    def search(self, term, lang):
        return tweepy.Paginator(self.api.search_recent_tweets , f"{term}  lang:{lang} -is:retweet", max_results = 100).flatten(limit=1000)