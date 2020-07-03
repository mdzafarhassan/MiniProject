from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookMaster, BlogPost
from managers.bulk_uploader import zip_uploader
from zipfile import ZipFile
import requests
from django.http import JsonResponse
from datetime import datetime
from .form import BookForm, BlogPostForm
from django.contrib.auth.decorators import login_required


def index(request):
    print("  >> HOME")
    context = {'home_page': True}
    return render(request, 'index.html', context)


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


def book(request, **kwargs):
    context = {'book_page': True}
    books = BookMaster.objectstem.all()
    context['books'] = books
    return render(request, 'books_home.html', context)


def add_book(request, **kwargs):
    context = {'add_book_page': True}
    action = kwargs.get('action')
    if action:
        filter = {}
        if action == 'delete':
            context['delete'] = True
            context['page_heading'] = 'Delete Book'
            filter['is_active'] = True
        if action == 'restore':
            context['restore'] = True
            context['page_heading'] = 'Restore Book'
            filter['is_active'] = False
        books = BookMaster.objects.filter(**filter).all()
        context['books'] = books
        return render(request, 'book_add.html', context)

    context['add'] = True
    context['page_heading'] = 'Add New Book'
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.is_active = True
        instance.created_date = str(datetime.now())[:19]
        instance.created_by = request.user
        instance.last_modified_date = str(datetime.now())[:19]
        instance.last_modified_by = request.user

        instance.save()
        return redirect("/")

    context['form'] = form
    return render(request, 'book_add.html', context)


def author(request, **kwargs):
    context = {'author_page': True}
    author = kwargs.get('name', None)
    if author:
        return render(request, 'author_page.html', context)
    else:
        context['author'] = author
        return render(request, 'author_home.html', context)


def blogs(request):
    context = {'blogs_home': True}
    posts = BlogPost.objects.all()
    context['posts'] = posts
    return render(request, 'blog_home.html', context)


def blog_add(request):
    context = {'blog_page': True}
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.is_active = True
        instance.created_by = request.user
        instance.created_date = str(datetime.now())[:19]
        instance.last_modified_date = str(datetime.now())[:19]

        instance.save()
        return redirect("/")

    context['form'] = form
    return render(request, 'blog_add.html', context)


# Testing/RnD and Debugging Views/Codes

def bulk_upload(request):
    return render(request, 'bulk_upload.html')


def test(request):
    from pprint import pprint
    context = {'test_page': True}

    books = list(BookMaster.objects.filter(book_type='Novel').annotate(test='book_genre').values(
        'book_name', 'book_type', 'book_genre', 'book_pages_count'))

    context['books'] = books
    pprint(context)

    return render(request, 'test.html', context)


def test2(request):
    context={}
    print("this is test funtion from vi")
    return render(request, 'test.html', context)
