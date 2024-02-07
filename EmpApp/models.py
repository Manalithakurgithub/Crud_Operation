from django.db import models
from django import forms
# Create your models here.
class Emp(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    address=models.TextField()
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    age=models.IntegerField()

    class Meta:
        db_table='Employee'

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'