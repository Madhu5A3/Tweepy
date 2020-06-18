import tweepy
import config
from tweepy.auth import OAuthHandler
import time

auth = OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user.name)
'''for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)'''
search = 'OpenSource'
nTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
