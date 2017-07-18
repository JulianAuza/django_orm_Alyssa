# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 10 :
            errors['course_name'] = 'Course names must be at least 10 characters'
        if len(post_data['desc']) < 15 :
            errors['description'] = 'Course descriptions must be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()