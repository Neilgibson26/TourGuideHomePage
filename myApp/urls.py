from django.urls import path
from . import views

app_name = 'myApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home2, name='home2'),
]