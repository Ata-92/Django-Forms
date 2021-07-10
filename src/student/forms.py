from django import forms
from django.forms import fields
from django.forms.fields import CharField
from .models import Student
# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label="Your name")
#     last_name = forms.CharField(max_length=100, label='Last Name')
#     number = forms.IntegerField(required = False)

class Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]
        labels = {"first_name": "Adınız"}
