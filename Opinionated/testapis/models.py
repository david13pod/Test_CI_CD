from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_negative(value):
    if value < 0 :
        raise ValidationError(
            _('%(value)s is not a positive number'),
            params=('value', value)
        )
class Classroom (models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField('testapis.Student')

    def __str__(self):
        return self.name

class Student (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.SlugField(blank=True, null=True)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True, validators=[validate_negative])

    def __str__(self):
        return self.firstname
    
    def get_grades(self):

        if self.average_score < 40:
            return 'fail'
        elif 40<= self.average_score < 70:
            return 'pass'
        elif 70<= self.average_score <= 100:
            return 'excellent'
        else:
            return 'error'
    
    def save(self, *args, **kwargs):
        self.username = slugify(self.firstname)
        print(self.username)
        super(Student,self).save(*args, **kwargs)

    @property
    def get_status(self):
        if self.average_score < 40:
            return 'not qualified'
        else:
            return 'qualified'