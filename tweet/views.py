from django.shortcuts import render, redirect
from django.views.generic import CreateView
# from django.conf import settings
from django.urls import reverse_lazy, reverse
from . import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime,timedelta
import time
import tweepy
from django.conf import settings
# User = settings.AUTH_USER_MODEL
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


# class RegisterView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
# def login_view(request):
#     user = None
#     if request.method =='POST':
#         oauth = tweepy.OAuthHandler(settings.TWEEPY_AUTH_TWITTER_KEY, 
#                 settings.TWEEPY_AUTH_TWITTER_SECRET)
#         # direct the user to the authentication url
#         # if user is logged-in and authorized then transparently goto       the callback URL
#         auth_url = oauth.get_authorization_url(True)
#         response = redirect(auth_url)
#         # store the request token
#         request.session['request_token'] = oauth.request_token
#         user = tweepy.API(oauth).me()
#         return response
#     return render(request, 'registration/login.html', {'user':user})
class NewTweetView(CreateView, LoginRequiredMixin):
    model = models.NewTweet
    form_class = forms.NewTweetForm
    template_name = 'new_tweet.html'
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     # new_tweet = request.POST04/04/2021 16:18
    #     made_on = datetime.strptime(request.POST.get('made_on'), '%d/%m/%Y %H:%M')
    #     created = datetime.strptime(request.POST.get('created'), '%Y-%m-%d %H:%M:%S.%f')
    #     created = created.strftime("%Y-%m-%d %H:%M")
    #     created = datetime.strptime(created, '%Y-%m-%d %H:%M')
    #     delta = made_on - created
    #     print('Time gap', delta)
    #     if delta > timedelta(0):
    #         time.sleep(delta.total_seconds())
    #     auth = tweepy.OAuthHandler(settings.TWEEPY_AUTH_TWITTER_KEY, 
    #         settings.TWEEPY_AUTH_TWITTER_SECRET)
    #     auth.set_access_token(settings.TWEEPY_ACCESS_TWITTER_KEY, 
    #         settings.TWEEPY_ACCESS_TWITTER_SECRET)

    #     api = tweepy.API(auth)

    #     try:
    #         # import pdb
    #         # pdb.set_trace()
    #         api.verify_credentials()
    #         api.update_status(request.POST.get('text_field'))
    #         print("Authentication OK")
    #         return redirect('home')
            
    #     except:
    #         print("Error during authentication")

        # from datetime import datetime
        # import pytz

        # # it will get the time zone
        # # of the specified location
        # IST = pytz.timezone('Asia/Kolkata')

        # datetime_ist = datetime.now(IST)
        # dt_string = datetime_ist.strftime('%Y:%m:%d %H:%M')


# def new_tweet_view(request):
#     if request.method == 'POST':
