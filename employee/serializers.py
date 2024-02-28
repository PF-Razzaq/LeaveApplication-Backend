from rest_framework import serializers
from .models import Employee,ApplyForLeave

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk', 'first_name', 'last_name', 'email','password', 'birthday', 'department','role','employee_id')


class ApplyForLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplyForLeave
        fields = ('pk','start_date','end_date','leave_type','reason')