from django.urls import path


urlpatterns = [
	path('registration/', RegisterView.as_view(), name='register_page_url')
]
