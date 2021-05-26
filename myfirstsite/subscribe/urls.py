from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
    path('hello', views.hello, name = 'hello'),
    path('login', views.regform, name = 'login'),
]