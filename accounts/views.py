###
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.text import slugify

from .forms import CustomUserCreationForm, LoginForm
from users_type.models import CustomUser
from .tokens import account_activation_token


###


###


###
### Validate email ###
###
### Sign up view ###

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            print(user.first_name, "#", user.last_name, "#", user.email)
            username = slugify(user.email.split('@')[0])  # generate a unique username based on the email
            user.username = username
            user.set_password(form.cleaned_data["password1"])
            user.save()
            ### User needs to verify email ###
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            verification_link = request.build_absolute_uri('/') + f'accounts/verify-email/{uidb64}/{token}/'
            from_email = 'oma.gonzales@gmail.com'
            email = EmailMessage('Verify your email address',
                                 f'Click this link to verify your email address: {verification_link}',
                                 from_email, to=[user.email])
            email.send()
            return redirect('accounts:email_user_needs_to_verify_email')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})


def email_user_needs_to_verify_email(request):
    return render(request, "account/email/email_confirmation_needed.html")


### users needs to verify their email first ###


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email address has been verified successfully.')
        return redirect('home')
    else:
        print("Email verification failed")
        if user is None:
            print("### User is none ###")
        messages.error(request, 'The verification link is invalid or has expired.')

        return render(request=request, template_name="account/email/email_verification_failed.html")


###


###

def send_email_new_registered_user(user_id):
    try:
        print("Enters send_email_new_registed_user try")
        profile = Profile.objects.latest('id')
        if profile:
            print("Se obtuvo profile")
        '''sending the order to the customer'''
        subject = f"Stickers Gallito Perú - Nuevo usuario registrado #{profile.id}"
        to = [f'{profile.user.email}', 'stickersgallito@gmail.com', 'oma.gonzales@gmail.com']
        from_email = 'stickersgallito@stickersgallito.pe'
        user_information = {
            'user_id': profile.user.id,
            'user_name': profile.user.username,
            'user_full_name': profile.user.get_full_name,
            'user_dni': profile.dni,
            'user_deparment': profile.shipping_deparment,
            'user_province': profile.shipping_province,
            'user_disctrict': profile.shipping_district,
            'user_shipping_address': profile.shipping_address1,
            'user_email': profile.user.email,
            'user_phone': profile.phone_number,
            'user_is_active': profile.user.is_active,
        }
        message = get_template('accounts/new_registered_user.html').render(user_information)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
        print("Se envió msj")
    except:
        pass


from django.http import JsonResponse
from django.contrib.auth import login, authenticate


###


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        print("### Request is post")

        if login_form.is_valid():
            print("### Request is VALID")
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            print("User name", username, "type: ", type(username))
            print("Pass", password, "type: ", type(password))
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponse(status=204, headers={'HX-Trigger': 'user_logged_in'})
        else:
            return render(request=request, template_name="account/email/login_form.html",
                          context={'login_form': login_form, 'errors': login_form.errors})

    else:
        login_form = LoginForm(request)
        context = {
            "login_form": login_form,
        }
        return render(request=request, template_name="account/email/login_form.html",
                      context={'login_form': login_form, 'errors': login_form.errors})



def logout_view(request):
    logout(request)
    return redirect('/')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Good Sheperd - Academia de inglés online',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'oma.gonzales@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("accounts:password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html",
                  context={"password_reset_form": password_reset_form})
