# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import User

def index(request):
    return render(request, 'lr_app/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email'] 
            password = request.POST['password']
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password_hash=password_hash)
            id = new_user.id
            messages.success(request, 'Successfully registered!')
            return redirect('/success/{}'.format(id))
    else:
        return redirect('/')

def authenticate(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Email not recognized.  Please register an account.')
            return redirect('/')
        entered_pw = request.POST['password']
        user_hash = user.password_hash
        if bcrypt.checkpw(entered_pw.encode(), user_hash.encode()):
            messages.success(request, 'Successfully logged in!')
            return redirect('/success/{}'.format(user.id))
        else:
            messages.error(request, 'Password incorrect.  Please try again!')
            return redirect('/')
    else:
        return redirect('/')
    
def success(request, id):
    user = User.objects.get(id=id)
    return render(request, 'lr_app/success.html', {'user': user})