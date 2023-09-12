from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={'placeholder': "Nombre De Usuario"}
            )
    )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={'placeholder': "Contraseña"}
            )
    )

    class Meta:
        model = User
        fields = ('username', 'password')
