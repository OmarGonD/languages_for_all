

from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import LoginForm



def login_form(request):
    return {'login_form': LoginForm()}


