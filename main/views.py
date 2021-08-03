from django.shortcuts import redirect
from django.views.generic import ListView

from product.models import Product


def redirect_home(request):
    return redirect('home_page_url', permanent=True)


class HomePageView(ListView):
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'
