# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import User

def index(request):
    return render(request, 'sr_users/index.html', {'users': User.objects.all()})

def show(request, id):
    user = User.objects.get(id=id)
    return render(request, 'sr_users/show.html', {'user':user})

def new(request):
    return render(request, 'sr_users/new.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email'] 
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
            id = new_user.id
            return redirect('/users/{}'.format(id))
    else:
        return redirect('/')

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'sr_users/edit.html', {'user':user})

def update(request, id):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/{}/edit'.format(id))
        else:
            user = User.objects.get(id=id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email'] 
            user.save()
            return redirect('/users/{}'.format(id))
    else:
        return redirect('/')

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')
