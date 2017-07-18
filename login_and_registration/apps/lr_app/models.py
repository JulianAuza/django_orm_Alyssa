# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

NAME_REGEX = re.compile(r'^[a-zA-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2 :
            errors['name_length'] = 'Names are required and must be no fewer than 2 characters'
        if not NAME_REGEX.match(post_data['first_name']) or not NAME_REGEX.match(post_data['last_name']) :
            errors['alpha_name'] = 'Names can only contain letters'
        if not EMAIL_REGEX.match(post_data['email']) :
            errors['invalid_email'] = 'Email address is invalid'
        if len(post_data['password']) == 0 or len(post_data['confirm']) == 0:
            errors['passwords_blank'] = 'Both password fields are required and must match'
        elif post_data['password'] != post_data['confirm']:
            errors['password_match'] = 'Passwords do not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256)
    password_hash = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
