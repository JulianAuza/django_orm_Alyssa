# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

# validators
def email_valid(email):
    if not validate_email(email):
        raise ValidationError('Invalid Email')

def 

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, validators=[email_valid])
    age = models.IntegerField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)