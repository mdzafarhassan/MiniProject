from django.contrib import admin
from .models import BookMaster
# Register your models here.


class BookMasterAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'book_type', 'book_genre', 'book_year')


admin.site.register(BookMaster, BookMasterAdmin)
