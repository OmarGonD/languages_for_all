from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import CourseOffering
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, unique=True)
    date_of_birth = models.DateField(null=False, blank=False, default='1980-01-01')
    photo = models.ImageField('foto', upload_to='images', null=True, blank=True, default='images/user.png')
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    widgets = {
        'my_date_field': DatePickerInput(),
        'my_time_field': TimePickerInput(),
        'my_date_time_field' : DateTimePickerInput(),
    }
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Teacher(CustomUser):
    is_teacher = models.BooleanField(default=True)
    courses = models.ForeignKey(CourseOffering, blank=True, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
