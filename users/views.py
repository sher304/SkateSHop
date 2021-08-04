from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from product.models import Product
from .forms import RegistrationForm


class RegisterView(CreateView):
	model = Product
	template_name = 'register.html'
	form_class = RegistrationForm


class LoginView(LoginView):
	template_name = 'login.html'
	success_url = reverse_lazy('home_page_url')
