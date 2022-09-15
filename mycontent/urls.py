from django.urls import path

from boook1 import settings
from mycontent import views

app_name = 'mycontent'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('book/<slug:book_slug>', views.book, name='book'),
    path('create/', views.book_create, name='book_create'),
    path('search_result/', views.search_result, name='search_result'),
]
