from django.forms import TextInput, PasswordInput, EmailInput
from django.contrib.auth.models import BaseUserManager, User


# Create your models here.


class RegisterForm(BaseUserManager):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2']
        widgets = {
            'firstname': TextInput(attrs={'class': 'form-control'}),
            'lastname': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }
