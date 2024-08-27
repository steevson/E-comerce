from . import views
from django.urls import path
urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
    path('minus_cart/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('cart_delete/<int:product_id>/', views.cart_delete, name='cart_delete'),
    path('checkout', views.checkout, name='checkout'),
    path('bankform', views.Bankform, name='bankform')

]
