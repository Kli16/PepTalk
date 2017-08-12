from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .forms import User
from .models import Profile


class SignUpFormMentees(UserCreationForm):
    age = forms.IntegerField()
    school = forms.CharField(max_length=40)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class SignUpFormMentors(UserCreationForm):
    age = forms.IntegerField()
    school = forms.CharField(max_length=40)
    avatar = forms.ImageField()
    facebook = forms.URLField()
    experience = forms.CharField(max_length=400)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class MentorsEditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Create your tests here.
