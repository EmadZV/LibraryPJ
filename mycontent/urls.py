from django.urls import path

from boook1 import settings
from mycontent import views

app_name = 'mycontent'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('book/<slug:book_slug>', views.book, name='book')
]