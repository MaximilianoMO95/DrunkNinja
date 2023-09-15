from django.contrib.auth.forms import (
        AuthenticationForm,
        UserCreationForm,
)

from .models import CustomerUser

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

