from django.forms import ModelForm

from mybook.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""

    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page',)
