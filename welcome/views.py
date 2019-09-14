from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Books


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

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
                print('Registration Completed')
                return redirect('/')
        else:
            messages.info(request, 'Password does not match')
            return redirect('/register')
    else:
        return render(request, 'register.html')


def books(request):
    return render(request, 'books_home.html')


# Testing/RnD and Debugging Views/Codes
def test(request):
    val = 'this is test value'
    return render(request, 'test.html', {'value': val})


def add(request):
    return render(request, 'add.html')


def result(request):
    a = request.GET['num1']
    b = request.GET['num2']
    val = int(a) + int(b)
    return render(request, 'result.html', {'result': val})