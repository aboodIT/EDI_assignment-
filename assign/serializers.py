from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Employee_model

class Employee_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_model
        fields = ('id','name','team','pay')