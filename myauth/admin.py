from django.contrib import admin

# Register your models here.
from myauth.models import Category, Author, Translator, Publisher, MyUser

admin.site.register(MyUser),
admin.site.register(Author),
admin.site.register(Translator),
admin.site.register(Publisher),


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ('status', 'publish')
