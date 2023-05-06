from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True)
    is_email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    photo = models.ImageField('foto', upload_to='images', null=True, blank=True)

    #def __str__(self):
    #    return self.email


#class Teacher(CustomUser):
    
