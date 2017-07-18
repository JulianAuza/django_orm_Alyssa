# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) == 0 or len(post_data['last_name']) == 0 or len(post_data['email']) == 0:
            errors['required']='All fields are required'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']='Invalid Email Address!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()