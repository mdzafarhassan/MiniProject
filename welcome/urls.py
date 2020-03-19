# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.register, name='Register'),
    path('login', views.login, name='Login'),
    path('logout', views.logout, name='Logout'),
    path('books', views.books, name='Books'),
    path('bulk-upload', views.bulk_upload, name='bulk_upload'),
    path('author', views.author, name='author'),
    path('author/<name>', views.author, name='author_page'),

    # Testing/RnD and Debugging Urls/Codes
    path('test', views.bulk_upload, name='Test'),
    path('result', views.result, name='Result'),
]

urlpatterns += staticfiles_urlpatterns()
