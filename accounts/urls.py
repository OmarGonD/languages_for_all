from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register_view, email_user_needs_to_verify_email, verify_email, login_view, logout_view, password_reset_request

app_name = 'accounts'

urlpatterns = [
    # ... other URL patterns ...
    path('email_verification_required/', email_user_needs_to_verify_email, name='email_user_needs_to_verify_email'),
    path('register/', register_view, name='register'),
    path('verify-email/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]

