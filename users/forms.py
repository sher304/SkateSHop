from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class RegistrationForm(forms.ModelForm):
    # username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirmation')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exists')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Invalid password')
        return data

    def save(self, commit=True):
        user = CustomUser.objects.create_user(**self.cleaned_data)
        return user
