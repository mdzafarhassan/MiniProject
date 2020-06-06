from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
import pytz
from datetime import datetime

# Create your views here.


def account(request):
    context = {"account_page": True}
    if request.method == "POST":
        username = request.user
        user = User.objects.get(username=username)
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email = request.POST['email_id']
        user.save()
        messages.info(request, 'Profile Information Updated')
        return redirect('/account')
    context['last_login'] = request.session.get('last_login')
    return render(request, 'account.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            lastlogin = user.last_login
            timezones = 'Asia/Kolkata'
            lastlogin = lastlogin.astimezone(pytz.timezone(timezones))
            request.session['last_login'] = str(lastlogin)

            auth.login(request, user)
            user_name = str(user)
            if user_name in ['admin', 'jags']:
                request.session['is_admin'] = True
            else:
                request.session['is_admin'] = False
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('Login')

    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':

        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email_id']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Username already in use')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password does not match')
            return redirect('/register')
    else:
        return render(request, 'register.html')
