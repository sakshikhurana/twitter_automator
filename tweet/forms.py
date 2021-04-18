from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.contrib.auth.models import User
from . import models
# class RegisterForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password')
#         help_texts = {
#             'username': None
#         }
#         widgets = {'password': forms.PasswordInput()}


class NewTweetForm(forms.ModelForm):
    class Meta:
        model = models.NewTweet
        fields = ['text_field', 'made_on']
        widgets = {'made_on': DateTimePickerInput()}
