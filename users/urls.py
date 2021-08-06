from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *


urlpatterns = [

	path('registration/', RegisterView.as_view(), name='register_page_url'),
	path('login/', LoginView.as_view(), name='login_page_url'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('users/', include('allauth.urls')),
]
