
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
app_name = 'tweet'
urlpatterns = [
    path('new',views.NewTweetView.as_view(), name='new'),
]
