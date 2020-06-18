import tweepy
from tweepy.auth import OAuthHandler
import time

auth = OAuthHandler('RvAikq5sj6tPD5K6HNR57oYnL', 'TMi8zdSZUs3u6QJUN63kGdXJ7h7OXOcVRXgilwGK6GyOLD5Cc4')
auth.set_access_token('878891720213016578-CllFoXUibZcujyZ6DZo1ZP4veVwpwao',
                     '7CAFwbxlaLvAtuGy0XHrWaDaNctu9mOgbug86xcD6zgHX')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user.name)
'''for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)'''
search = 'OpenSource'
nTweets=500

for tweet in tweepy.Cursor(api.search, search).items(nTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

