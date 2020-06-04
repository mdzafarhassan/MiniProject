from django import forms
from .models import BookMaster


class BookForm(forms.ModelForm):
    class Meta:
        model = BookMaster
        fields = [
            "book_type",
            "book_name",
            "book_author",
            "book_genre",
            "book_year",
            "book_publications",
            "book_pages_count",
            "book_front_cover",
        ]
