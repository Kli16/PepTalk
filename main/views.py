# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User, AbstractBaseUser, UserManager
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpFormMentees, SignUpFormMentors, MentorsEditProfileForm
from .models import Profile
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'main/about.html')

def mentee_signup(request):
    if request.method == 'POST':
        form = SignUpFormMentees(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.age = form.cleaned_data.get('age')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            #profile.school = form.cleaned_data.get('school')
            #user.profile.age = form.cleaned_data.get('age')
            #user.profile.avatar = form.cleaned_data.get('avatar')
            #user = uform.save()
            #user.save()
            group = Group.objects.get(name="Mentees")
            user.groups.add(group)
            #Profile_Holder = user
            #user = User.objects.create_user(
            #    username = form.cleaned_data.get('username'),
            #    email = form.cleaned_data.get('email'),
            #    password = form.cleaned_data.get('password1'),
            #)
            return redirect('../mentee')
    else:
        form = SignUpFormMentees()
    return render(request, 'main/signup.html', {'form':form})

def mentor_signup(request):
    if request.method == 'POST':
        form = SignUpFormMentors(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.age = form.cleaned_data.get('age')
            user.profile.school = form.cleaned_data.get('school')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.facebook = form.cleaned_data.get('facebook')
            user.profile.experience = form.cleaned_data.get('experience')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            #profile.school = form.cleaned_data.get('school')
            #user.profile.age = form.cleaned_data.get('age')
            #user.profile.avatar = form.cleaned_data.get('avatar')
            #user = uform.save()
            #user.save()
            #Profile_Holder = user
            #user = User.objects.create_user(
            #    username = form.cleaned_data.get('username'),
            #    email = form.cleaned_data.get('email'),
            #    password = form.cleaned_data.get('password1'),
            #)
            return redirect('../mentorsubmission')
    else:
        form = SignUpFormMentors()
    return render(request, 'main/signup.html', {'form':form})

def is_mentee(user):
    return user.groups.filter(name='Mentees').exists()

def is_mentor(user):
    return user.groups.filter(name='Mentors').exists()

@login_required
@user_passes_test(is_mentee)
def mentee(request):
    return render(request, 'main/mentee.html')

@login_required
@user_passes_test(is_mentor)
def mentor(request):
    return render(request, 'main/mentor.html')

def mentees_about(request):
    return render(request, 'main/mentees_about.html')

def mentors_about(request):
    return render(request, 'main/mentors_about.html')

def contact(request):
    return render(request, 'main/contact.html')

def login_success(request):
    """
    Redirects users based on whether they are mentors or mentees
    """
    if request.user.groups.filter(name="Mentees").exists():
        return redirect("mentee")
    if request.user.groups.filter(name="Mentors").exists():
        return redirect("mentor")

@login_required
@user_passes_test(is_mentor)
def mentor_profile(request):
    args = {'user': request.user}
    #user = User.objects.get(username=username)
    return render(request, 'main/mentor_profile.html', args)

@login_required
@user_passes_test(is_mentee)
def mentee_profile(request):
    args = {'user': request.user}
    #user = User.objects.get(username=username)
    return render(request, 'main/mentee_profile.html', args)

@login_required
@user_passes_test(is_mentee)
def get_mentor_profile(request, username):
    #args = {'user': request.user}
    user = User.objects.get(username=username)
    return render(request, 'main/get_mentor_profile.html', {'user':user})

@login_required
@user_passes_test(is_mentee)
def generalcontact(request):
    return render(request, 'main/generalcontact.html')

@login_required
def prepsharing(request):
    if request.user.groups.filter(name='Mentees').exists():
        return render(request, 'main/menteeprepsharing.html')
    if request.user.groups.filter(name='Mentors').exists():
        return render(request, 'main/mentorprepsharing.html')

@login_required
def drills(request):
    if request.user.groups.filter(name='Mentees').exists():
        return render(request, 'main/menteedrills.html')
    if request.user.groups.filter(name='Mentors').exists():
        return render(request, 'main/mentordrills.html')

@login_required
def tournament(request):
    if request.user.groups.filter(name='Mentees').exists():
        return render(request, 'main/menteetournament.html')
    if request.user.groups.filter(name='Mentors').exists():
        return render(request, 'main/mentortournament.html')

@login_required
@user_passes_test(is_mentor)
def edit_mentor_profile(request):
    if request.method == 'POST':
        form = MentorsEditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = MentorsEditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'main/edit_mentor_profile.html', args)

def submitted(request):
    return render(request, 'main/submitted.html')
# Create your views here.
