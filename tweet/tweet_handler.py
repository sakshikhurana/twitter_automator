import logging
import arrow
import os
import tweepy
from django.conf import settings
from .models import NewTweet

logger = logging.getLogger(__name__)


def send_tweets(consumer_key, consumer_secret, access_token,
                access_token_secret):
    expired_tweets = NewTweet.objects.filter(sent=False,
        made_on__lte=arrow.utcnow().to('Asia/Calcutta').datetime)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    if expired_tweets.count() == 0:
        logging.info("No tweet to send as of now")
    for db_tweet in expired_tweets:
        logging.info('sending tweet')
        try:
            api.update_status(db_tweet.text_field)
            db_tweet.sent = True
            db_tweet.save()
            logging.info('tweet sent')
        except tweepy.TweepError as error:
            if error.api_code == 187:
                # Do something special
                print('duplicate message')
            else:
                raise error       
        
        


def tweet_scheduler():
    # if (os.environ.get('CONSUMER_KEY') or os.environ.get('CONSUMER_SECRET') or
    #    os.environ.get('ACCESS_TOKEN') or os.environ.get('TOKEN_SECRET')):
    # import environ
    # # Initialise environment variables
    # env = environ.Env()
    # environ.Env.read_env()
    # consumer_key = env('TWEEPY_AUTH_TWITTER_KEY')
    # consumer_secret = env('TWEEPY_AUTH_TWITTER_SECRET')
    # access_token = env('TWEEPY_ACCESS_TWITTER_KEY')
    # access_token_secret = env('TWEEPY_ACCESS_TWITTER_SECRET')
    consumer_key = settings.TWEEPY_AUTH_TWITTER_KEY
    consumer_secret = settings.TWEEPY_AUTH_TWITTER_SECRET
    access_token = settings.TWEEPY_ACCESS_TWITTER_KEY
    access_token_secret = settings.TWEEPY_ACCESS_TWITTER_SECRET
    send_tweets(consumer_key, consumer_secret,
                access_token, access_token_secret)
    # else:
    #     raise NotImplementedError('Set environment variables correctly')
