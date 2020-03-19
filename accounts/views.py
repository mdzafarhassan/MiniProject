from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.


def account(request):
    print('account')
    if request.user.is_authenticated():
        print('User')
        return redirect('/')
    else:
        print('Not Login')
        return redirect('/')
