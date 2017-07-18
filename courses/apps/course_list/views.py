# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'course_list/index.html', {'courses': courses})

def create(request):
    if request.method == 'POST':
        errors = Course.objects.course_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            new_course = Course.objects.create(name=name, desc=desc)
        return redirect('/')
    else:
        return redirect('/')

def remove(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course_list/remove.html', {'course': course})

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
