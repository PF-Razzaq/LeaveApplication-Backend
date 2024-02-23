from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    birthday = models.DateField()
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
