from django.urls import path

from .views import *
from . import views


urlpatterns = [
    path('product/create', CreateProductView.as_view(), name='create_product_url'),
    path('product/update/<int:id>/', UpdateProductView.as_view(), name='update_product_url'),
    path('product/delete/<int:id>/', DeleteProductView.as_view(), name='delete_product_url'),

    # cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add_url'),
    path('cart/item-clear/<int:id>/', views.item_clear, name='item_clear_url'),
    path('cart/item-increment/<int:id>/', views.item_increment, name='item_increment_url'),
    path('cart/item-decrement/<int:id>/', views.item_decrement, name='item_decrement_url'),
    path('cart/cart-clear/', views.cart_clear, name='cart_clear_url'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail_url'),

]
