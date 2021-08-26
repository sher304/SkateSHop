from cart import cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from .forms import *


def LikeView(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('product_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('product_detail_url', args=[str(pk)]))


class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse('product_detail_url', kwargs={'pk': self.kwargs['pk']})


class CheckoutView(CreateView):
    model = Checkout
    template_name = 'product_buy.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Cart.total
        return context

    def get_success_url(self):
        a = Cart(self.request)
        a.clear()
        return reverse('home_page_url')


class SearchListView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            return Product.objects.none()
        queryset = queryset.filter(Q(name__icontains=q))
        return queryset


class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class CreateProductView(IsAdminMixin, CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class = CreateProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('home_page_url')


class UpdateProductView(IsAdminMixin, UpdateView):
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


class DeleteProductView(IsAdminMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home_page_url')


class Cart(cart.Cart):
    total = 0

    def add(self, product, quantity=1, action=None):
        super().add(product, quantity, action)
        Cart.total += product.price
        self.save()

    def decrement(self, product):
        Cart.total -= product.price
        super().decrement(product)
        self.save()

    def remove(self, product):
        Cart.total -= product.quantity * product.price
        super().remove(product)
        self.save()

    def clear(self):
        Cart.total = 0
        super().clear()

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
    return render(request, 'cart_detail.html', {'total': Cart.total})

