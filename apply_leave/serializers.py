from .models import ApplyForLeave
from rest_framework import serializers

class ApplyForLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplyForLeave
        fields = '__all__'