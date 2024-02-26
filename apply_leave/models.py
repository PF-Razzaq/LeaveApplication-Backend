from django.db import models

# Create your models here.
class ApplyForLeave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.TextField(max_length=30)
    reason = models.TextField(max_length=30)

def __str__(self):
    return f"{self.leave_type} {self.reason}"