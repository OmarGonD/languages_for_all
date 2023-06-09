from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users_type.models import CustomUser
from django.contrib.auth.models import User
from users_type.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
###

from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django import forms
from django.shortcuts import redirect
from users_type.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['first_name'].label = 'Nombre(s)'
        self.fields['last_name'].label = 'Apellidos'
        self.fields['phone'].label = 'Teléfono'
        self.fields['country'].label = 'País'
        self.fields['city'].label = 'Ciudad'
        self.fields['photo'].required = False

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=DatePickerInput, label='Fecha de nacimiento')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'phone', 'date_of_birth',  'password1', 'password2', 'country', 'city', 'photo')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class RegistrationForm(forms.Form):
    #Create a form with the following fields: name, last_name, email, country, phone_number, document_type, document, language, starting_date, checkbox_1, checkbox_2
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-field'}))
    country = CountryField(blank_label='(Elige su país)')
    phone_number = forms.CharField(label='Celular', max_length=20, widget=forms.TextInput(attrs={'class': 'form-field'}))
    date_of_birth = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'class': 'form-field'}))
    DOCUMENT_CHOICES = [
        ('dni', 'DNI'),
        ('carne_extrajeria', 'Carné extranjería'),
        ('Pasaporte', 'Pasaporte')
    ]
    document_type = forms.ChoiceField(choices=DOCUMENT_CHOICES, label='Tipo de documento de identidad', widget=forms.Select(attrs={'class': 'form-field'}))
    document = forms.CharField(label='Documento', max_length=30, widget=forms.TextInput(attrs={'class': 'form-field'}))
    LANGUAGE_CHOICES = [
        ('english', 'Inglés'),
    ]
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Idioma a aprender', widget=forms.Select(attrs={'class': 'form-field'}))
    SEMESTER_CHOICES = [
        ('this_semester', 'This Semester'),
        ('next_year', 'Next Year'),
    ]
    starting_date = forms.ChoiceField(choices=SEMESTER_CHOICES, label='Fecha de inicio', widget=forms.Select(attrs={'class': 'form-field'}))
    photo = forms.ImageField(label='Foto', required=False)
    HELP_TEXT_1 = "Otorgo mi consentimiento para el uso de mis datos personales."
    HELP_TEXT_2 = "Autorizo a Idiomas Católica a enviarme información general sobre los servicios de enseñanza de idiomas y servicios vinculados que ofrece."
    checkbox_1 = forms.BooleanField(required=False, label='', help_text=HELP_TEXT_1)
    checkbox_2 = forms.BooleanField(required=False, label='', help_text=HELP_TEXT_2)


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))



