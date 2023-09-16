from django import forms
from django.contrib.auth.forms import (
        AuthenticationForm,
        UserCreationForm
)

from .models import Customer, User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    shipping_address = forms.CharField(max_length=255)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'DD-MM-YYYY'})
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2', 'shipping_address', 'date_of_birth')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']


class CustomerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
            widget=forms.DateInput(format='%d-%m-%Y', attrs={'read-only': True, 'disabled': True})
    )

    class Meta:
        model = Customer
        fields = ('shipping_address', 'date_of_birth')
