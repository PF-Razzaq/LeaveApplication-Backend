from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    birthday = models.DateField()
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ApplyForLeave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.TextField(max_length=30)
    reason = models.TextField(max_length=30)

    def __str__(self):
        return f"{self.leave_type} {self.reason}"

    
