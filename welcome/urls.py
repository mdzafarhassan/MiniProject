# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.register, name='Register'),
    path('login', views.login, name='Login'),
    path('logout', views.logout, name='Logout'),
    path('books', views.books, name='Books'),

    # Testing/RnD and Debugging Urls/Codes
    path('test', views.test, name='Test'),
    path('add', views.add, name='Add'),
    path('result', views.result, name='Result'),
]
