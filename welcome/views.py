from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import BookMaster
from managers.bulk_uploader import zip_uploader
from zipfile import ZipFile


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
    context = {}
    books = BookMaster.objects.all()
    context['books'] = books
    return render(request, 'books_home.html', context)


def author(request, **kwargs):
    context = {}
    print(request, "  ::  ", kwargs)
    author = kwargs.get('name', 0)
    print(author)
    if not author:
        print('if')
        return render(request, 'author_home.html', context)
    else:
        print('else')
        context['author'] = author
        return render(request, 'author_page.html', context)


def bulk_upload(request):
    return render(request, 'bulk_upload.html')


# Testing/RnD and Debugging Views/Codes
def test(request):
    print(request)
    print("Hello World")
    books = BookMaster.objects.all()

    context = {"media": "abc.png"}
    val = 'this is test value'
    return render(request, 'test.html', {'books': books})


def add(request):
    return render(request, 'add.html')


def result(request):
    a = request.GET['num1']
    b = request.GET['num2']
    val = int(a) + int(b)
    return render(request, 'result.html', {'result': val})