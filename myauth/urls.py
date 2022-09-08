from django.contrib.auth import views
from django.urls import path, include
from .views import sign_up
app_name = 'myauth'
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('sign_up/', sign_up, name='sign_up'),

]
