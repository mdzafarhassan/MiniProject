# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.book, name='books'),
    path('add_book', views.add_book, name='add_book'),
    path('add_book/<action>', views.add_book, name='add_book_action'),
    path('authors', views.author, name='authors'),
    path('author/<name>', views.author, name='author_page'),
    path('blogs', views.blog, name="blogs"),
    path('weather', views.weather, name='weather'),
    path('bulk-upload', views.bulk_upload, name='bulk_upload'),

    # Testing/RnD and Debugging Urls/Codes
    path('test', views.test, name='Test'),
]

urlpatterns += staticfiles_urlpatterns()
