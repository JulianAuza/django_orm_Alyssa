# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    def __repr__(self):
        return "<Blog object: {} - {}, {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    desc = models.TextField()
    def __repr__(self):
        return "<Blog object: {} - {}, {}>".format(self.first_name, self.last_name, self.dojo.name)