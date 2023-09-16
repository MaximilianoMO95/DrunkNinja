from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import (CustomerProfileForm, UserLoginForm, UserRegistrationForm, UserUpdateForm)
from .models import Customer

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(View):
    template_name = 'users/signin.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            customer_group, _ = Group.objects.get_or_create(name='customer')
            user.groups.add(customer_group)

            customer = Customer(user=user, shipping_address=form.cleaned_data['shipping_address'], date_of_birth=form.cleaned_data['date_of_birth'])
            customer.save()

            login(request, user)

            return redirect('index')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class UserProfileView(View, PermissionRequiredMixin):
    permission_required = ('users.view_customer_profile', 'users.edit_customer_profile')
    template_name = 'users/profile.html'

    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = CustomerProfileForm(instance=request.user.customer)

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        profile_form = CustomerProfileForm(request.POST, instance=request.user.customer)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        profile_form.fields['date_of_birth'].disabled = True
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('users:profile')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})
