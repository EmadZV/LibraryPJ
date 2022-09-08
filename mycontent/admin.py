from django.contrib import admin
from .models import Book, VoteModel

# Register your models here.

admin.site.register(VoteModel),


@admin.register(Book)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'publisher', 'created', 'translator')
    prepopulated_fields = {'slug': ('title',)}
