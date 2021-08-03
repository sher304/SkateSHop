from django.shortcuts import render
from django.views.generic import CreateView

from product.models import Product
from .forms import RegistrationForm


class RegisterView(CreateView):
	model = Product
	template_name = 'register.html'
	form_class = RegistrationForm
