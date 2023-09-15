from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import CustomerUser
from .forms import (
        UserLoginForm,
        UserRegistrationForm,
)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

class UserRegistrationView(CreateView):
    model = CustomerUser
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Registracion exitosa!'
