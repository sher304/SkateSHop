from django.urls import path

from main.views import redirect_home
from .views import *
from . import views


urlpatterns = [

    path('', redirect_home),
    path('product/', ProductListView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_url'),
    path('product/like/<int:pk>/', LikeView, name='like_product_url'),
    path('product/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment_url'),
    path('product/create', CreateProductView.as_view(), name='create_product_url'),
    path('product/update/<int:id>/', UpdateProductView.as_view(), name='update_product_url'),
    path('product/delete/<int:id>/', DeleteProductView.as_view(), name='delete_product_url'),
    path('search', SearchListView.as_view(), name='search_product_url'),
    path('product/buy/', CheckoutView.as_view(), name='product_buy_url'),
    # cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add_url'),
    path('cart/item-clear/<int:id>/', views.item_clear, name='item_clear_url'),
    path('cart/item-increment/<int:id>/', views.item_increment, name='item_increment_url'),
    path('cart/item-decrement/<int:id>/', views.item_decrement, name='item_decrement_url'),
    path('cart/cart-clear/', views.cart_clear, name='cart_clear_url'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail_url'),

]

