from rest_framework import serializers
from .models import Employee,ApplyForLeave

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ApplyForLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplyForLeave
        fields = '__all__'