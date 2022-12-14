from django import forms
from .models import Book, Comment


class BookCreateForm(forms.ModelForm):
    cover = forms.ImageField(required=False)

    class Meta:
        model = Book
        fields = ('title', 'description', 'cover',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.ModelForm):
    author = forms.CharField(max_length=20, required=False)
    title = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Book
        fields = ('title', 'author')
