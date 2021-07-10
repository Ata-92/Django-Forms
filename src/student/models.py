from django.db import models

# Create your models here.
class StudentForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    number = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
