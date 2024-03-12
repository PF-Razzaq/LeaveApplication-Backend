from django.db import models
from datetime import timedelta


class Employee(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    birthday = models.DateField()
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ApplyForLeave(models.Model):


    PENDING = 0
    APPROVED = 1
    REJECTED = 2

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.TextField(max_length=30)
    reason = models.TextField(max_length=30)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING) 
    days = models.IntegerField(default=0)
    reject_reason = models.TextField(default='') 

    def save(self, *args, **kwargs):
        days = sum(
            1 for index in range((self.end_date - self.start_date).days + 1)
            if (self.start_date + timedelta(days=index)).weekday() not in [5, 6]
        )

        self.days = days

        super(ApplyForLeave, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.leave_type} {self.reason}"

    
