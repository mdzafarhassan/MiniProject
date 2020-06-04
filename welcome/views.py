from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookMaster
from managers.bulk_uploader import zip_uploader
from zipfile import ZipFile
import requests
from django.http import JsonResponse
from datetime import datetime

from .form import BookForm
from .models import BookMaster

from pprint import pprint


def index(request):
    return render(request, 'index.html')


def weather(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?lat=28.641942&lon=77.035342&appid=613a7f7cb40ea901b1008c5c9330dd4f&units=metric'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi,Delhi,India&appid=613a7f7cb40ea901b1008c5c9330dd4f&units=metric'

    x = requests.get(url).json()

    test = f'''
    <img src="http://openweathermap.org/img/w/{x['weather'][0]['icon']}.png" alt="image" />{x['main']['temp']}°C
        <ul>
            <li><b>{x['name']}</b></li>
            <li>{x['weather'][0]['description']}</li>
            <li> Feels <b>{x['main']['feels_like']}°C</b></li>
        </ul>
    '''
    return HttpResponse(test)


def books(request):
    context = {}
    books = BookMaster.objects.all()
    context['books'] = books
    return render(request, 'books_home.html', context)


def add_book(request):
    context = {}
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.created_date = str(datetime.now())[:19]
        instance.created_by = request.user
        instance.last_modified_date = str(datetime.now())[:19]
        instance.last_modified_by = request.user

        instance.save()
        return redirect("/")

    context['form'] = form
    return render(request, 'add_book.html', context)


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
