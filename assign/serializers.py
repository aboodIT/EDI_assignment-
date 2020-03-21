from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import employee_model, team_model, work_model, leaders_model

class employee_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee_model
        fields = ('id','url','name','team','leader','arrangment')

class team_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team_model
        fields = ('id','url','name')

class work_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = work_model
        fields = ('id','url','name')

class leader_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = leaders_model
        fields = ('id','url','name')

