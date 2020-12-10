from django.urls import path
from myapp import views

app_name='myapp'

urls = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]