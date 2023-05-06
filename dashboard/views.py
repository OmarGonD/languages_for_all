from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.text import slugify



def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")