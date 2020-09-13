from django.contrib import admin
from django.urls import path
from weatherapp import views

urlpatterns = [
    path('',views.weatherinfo,name='weather'),
    path('delete/<city_name>',views.delete_city,name='delete_city')
]
