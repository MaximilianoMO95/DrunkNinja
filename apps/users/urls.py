from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView
)

from .views import (UserLoginView, UserRegistrationView, UserProfileView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signin/', UserRegistrationView.as_view(), name='signin'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(template_name="users/password_change.html", success_url=reverse_lazy('users:profile')), name='password_change'),

    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html', success_url='done'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
