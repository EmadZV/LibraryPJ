from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from django import forms

from .models import Category

User = get_user_model()


class MyUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#
#     username = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': '',
#             'id': 'hi',
#         }
#     ))
