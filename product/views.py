from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from .models import Product
from .forms import *



class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'


class CreateProductView(CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class = CreateProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('home_page_url')


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = UpdateProductForm
    context_object_name = 'product_form'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('home_page_url')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        return reverse('home_page_url')


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('home_page_url')


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail_url')


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart_detail_url')


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail_url')


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail_url')


@login_required()
def cart_detail(request):
    return render(request, 'cart_detail.html')
