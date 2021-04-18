from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import tweepy
# Create your models here.


class NewTweet(models.Model):
    text_field = models.TextField(max_length=120)
    made_on = models.DateTimeField('date published')
    created_on = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text_field)


# @receiver(post_save, sender=NewTweet)
# def tweet_post(sender, instance, **kwargs):
#     twitter_auth_keys = {
#         "consumer_key": settings.TWEEPY_AUTH_TWITTER_KEY,
#         "consumer_secret": settings.TWEEPY_AUTH_TWITTER_SECRET,
#         "access_token": settings.TWEEPY_ACCESS_TWITTER_KEY,
#         "access_token_secret": settings.TWEEPY_ACCESS_TWITTER_SECRET
#     }

#     auth = tweepy.OAuthHandler(
#         twitter_auth_keys['consumer_key'],
#         twitter_auth_keys['consumer_secret']
#     )
#     auth.set_access_token(
#         twitter_auth_keys['access_token'],
#         twitter_auth_keys['access_token_secret']
#     )
#     api = tweepy.API(auth)

#     try:
#         import time
#         from datetime import datetime, timedelta
#         import pdb
#         pdb.set_trace()
#         delta = instance.made_on - instance.created_on
#         print('Time gap', delta)
#         if delta > timedelta(0):
#             time.sleep(delta.total_seconds())
#         api.update_status(instance.text_field)
#     except tweepy.TweepError as error:
#         if error.api_code == 187:
#             print('duplicate message')
