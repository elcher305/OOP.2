from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label="ФИО")
    email = forms.EmailField(label="Email")
    agreement = forms.BooleanField(label="Согласие на обработку персональных данных")

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'agreement']

class LoginForm(AuthenticationForm):
    pass