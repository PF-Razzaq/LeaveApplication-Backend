from django.db import models
from datetime import timedelta


class LeaveTable(models.Model):
    total_leave = models.IntegerField(default=24)
    approved_days = models.IntegerField(default=0)
    pending_leaves = models.IntegerField(default=24)

    def save(self, *args, **kwargs):
        self.pending_leaves = self.total_leave - self.approved_days
        super(LeaveTable, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}" 


class Employee(models.Model):
    leave_table = models.ForeignKey(LeaveTable, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
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

    FULL_LEAVE = 'Full Leave'
    HALF_LEAVE = 'Half Leave'

    LEAVE_CHOICES = [
        (FULL_LEAVE, 'Full Leave'),
        (HALF_LEAVE, 'Half Leave'),
    ]

    leave_table = models.ForeignKey(LeaveTable, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.TextField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    days = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    reject_reason = models.TextField(default='')
    leave_entries = models.CharField(max_length=20, choices=LEAVE_CHOICES, default="Full Leave")

    def save(self, *args, **kwargs):
        if self.leave_entries == self.FULL_LEAVE:
            days = sum(
                1 for index in range((self.end_date - self.start_date).days + 1)
                if (self.start_date + timedelta(days=index)).weekday() not in [5, 6]
            )
        elif self.leave_entries == self.HALF_LEAVE:
            days = sum(
                0.5 for index in range((self.end_date - self.start_date).days + 1)
                if (self.start_date + timedelta(days=index)).weekday() not in [5, 6]
            )
        else:
            days = 0

        self.days = days
        super(ApplyForLeave, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.leave_type}, {self.reject_reason}"
