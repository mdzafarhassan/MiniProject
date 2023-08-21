# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.account, name='account'),
    path('change-password', views.change_password, name='change_password')
]

urlpatterns += staticfiles_urlpatterns()
