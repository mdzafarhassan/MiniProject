from django.contrib import admin
from .models import BookMaster, BlogPost, BlogCategory
# Register your models here.


class BookMasterAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author',
                    'book_type', 'book_genre', 'book_year')


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tags', 'content', 'privacy_level')


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'cat_desc', 'is_active', 'created_by')


admin.site.register(BookMaster, BookMasterAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
