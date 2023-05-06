from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard_view

app_name = 'dashboard'

urlpatterns = [
    # ... other URL patterns ...
    path('', dashboard_view, name='dashboard_view'),

]
