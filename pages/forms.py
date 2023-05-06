from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column




class LanguageForm(forms.Form):
    LANGUAGES = [
        ('english', 'English'),
        ('spanish', 'Spanish'),
        ('korean', 'Korean'),
    ]
    language = forms.ChoiceField(choices=LANGUAGES)


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-field'}))
    country = CountryField(blank_label='(Elige su país)')
    phone_number = forms.CharField(label='Celular', max_length=20, widget=forms.TextInput(attrs={'class': 'form-field'}))
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
    HELP_TEXT_1 = "Otorgo mi consentimiento para el uso de mis datos personales."
    HELP_TEXT_2 = "Autorizo a Idiomas Católica a enviarme información general sobre los servicios de enseñanza de idiomas y servicios vinculados que ofrece."
    checkbox_1 = forms.BooleanField(required=False, label='', help_text=HELP_TEXT_1)
    checkbox_2 = forms.BooleanField(required=False, label='', help_text=HELP_TEXT_2)
