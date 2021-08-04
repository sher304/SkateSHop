from django.urls import path


from .views import *

urlpatterns = [
    path('product/create', CreateProductView.as_view(), name='create_product_url'),
    path('product/update/', UpdateProductView.as_view(), name='update_product_url'),
]

