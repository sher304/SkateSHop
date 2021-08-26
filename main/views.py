import datetime

from django.shortcuts import redirect
from django.views.generic import ListView

from product.models import Product


def redirect_home(request):
    return redirect('home_page_url', permanent=True)


class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    # paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        time_threshold = datetime.datetime.now() - datetime.timedelta(hours=1)
        context['products'] = Product.objects.filter(add_date__gt=time_threshold)
        return context
