# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#class User(models.Model):
#    username = models.CharField(max_length=20, default='')
#    email = models.EmailField(max_length=254)
#    first_name = models.CharField(max_length=20)
#    last_name = models.CharField(max_length=20)
    #Profile_Holder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=40,default='', blank=True)
    age = models.IntegerField(default=0, blank=True)
    avatar = models.ImageField(upload_to='media/images/avatars/', null=True, blank=True)
    facebook = models.URLField(max_length=500, blank=True)
    experience = models.CharField(max_length=400, blank=True, default='')
    debateexpertise = models.CharField(max_length=400, blank=True, default='')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
# Create your models here.
