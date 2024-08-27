from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index,name='index'),
    path('search', views.search, name='search'),
    path('<slug:cslug>/', views.index,name='product_cate'),
    path('<slug:cslug>/<slug:pslug>', views.details, name='details'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='home'),
    ]
