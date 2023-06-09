
from django.db import models

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


LEVELS = (
    ("BASIC", "basic"),
    ("INTERMIDIATE", "Intermediate"),
    ("ADVANCE", "Advance"),
)

class Level(models.Model):
    level = models.CharField(max_length=9,
                             choices=LEVELS,
                             default="BASIC")
    created_at = models.DateTimeField(auto_now_add=True)


class Vocabulary(models.Model):
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    language = models.CharField(max_length=50)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CourseOffering(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True) # assuming there's a teacher model already
    zoom_link = models.CharField(max_length=500)
    zoom_id = models.CharField(max_length=100)
    zoom_password = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.TimeField()
    semester = models.CharField()
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    score = models.IntegerField()
    rate = models.IntegerField()









"""also you dont want an fk to student in course - 
that would only allow a single student to take a course. 
You probably want a student to CourseOffering m2m. 
even more likely you want an m2m through table to capture such things
 as grade, attendance anything else that belongs to the pair of student and course they are taking"""