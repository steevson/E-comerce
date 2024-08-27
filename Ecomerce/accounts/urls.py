from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('account', views.login, name='account'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

]