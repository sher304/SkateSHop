from django import forms

from .models import *


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'status', 'price', 'description', 'image', 'category']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'user', 'product')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['region', 'name', 'surname', 'number', 'address', 'postcode', 'type_order']

