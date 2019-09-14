from django.db import models


class Books(models.Model):
    book_type = models.CharField(max_length=50)
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=50)
    book_year = models.CharField(max_length=4)
    book_publications = models.CharField(max_length=100)
    book_pages_count = models.IntegerField()
    book_front_cover = models.ImageField()
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.CharField(max_length=10)

    class Meta:
        db_table = "book_master"
