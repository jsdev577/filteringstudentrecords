from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    # countrys=(('INDIA',"India"),
    # ('GERMANY',"Germany"),
    # ('FRANCE',"France"),
    # ('ARGENTINA',"Argentina"),
    # ('PARAGUAY',"Paraguay"))
    # country=models.CharField(max_length=200,choices=countrys)
    country =CountryField()
    
    school=models.CharField(max_length=200)
    graduates=(('Garduate','True'),('Non-Graduate','False'))
    graduate=models.CharField(max_length=12,choices=graduates,default='Non-Graduate')
    def __str__(self):
        return self.student_name
