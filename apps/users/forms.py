from django import forms
from datetime import date
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

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        
        if age < 18:
            raise forms.ValidationError("Debes tener al menos 18 años para registrarte.")
        return dob

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
