from django import forms
from django.forms.fields import CharField

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Your name")
    last_name = forms.CharField(max_length=100, label='Last Name')
    number = forms.IntegerField(required = False)
