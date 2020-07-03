from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class BookMaster(models.Model):
    book_type = models.CharField(max_length=50)
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=50)
    book_year = models.CharField(max_length=4)
    book_publications = models.CharField(max_length=100)
    book_pages_count = models.IntegerField()
    book_front_cover = models.ImageField()
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.CharField(max_length=10)

    class Meta:
        db_table = "book_master"

    def __str__(self):
        return self.book_name


class BlogCategory(models.Model):
    cat_id = models.CharField(max_length=10, unique=True)
    cat_desc = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.CharField(max_length=10)

    class Meta:
        db_table = "blog_category"

    def __str__(self):
        return self.cat_id


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        BlogCategory, default=None, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    privacy_level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    last_modified_date = models.DateTimeField()

    class Meta:
        db_table = "blog_post"

    def __str__(self):
        return self.title

    @property
    def author(self):
        user = self.created_by
        author = {'username': user.username,
                  'first_name': user.first_name,
                  'last_name': user.last_name}
        return author

    @property
    def cat_desc(self):
        return self.category.cat_desc
