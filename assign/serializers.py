from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import employee_model, team_model

# class team_serializer(serializers.ModelSerializer):
#     #employee = employee_serializer(source='name')
#     class Meta:
#         model = team_model
#         fields = ('id','url','name')

class employee_serializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField("get_rate")
    class Meta:
        model = employee_model
        # fields = ('id','url','name','team','leader','pay')
        fields = ('id','name','team','leader','work_time','pay','rate',)

    def get_rate(self,obj):
        base = obj.pay*(obj.work_time/100)*40
        if obj.leader==True:
            rate = base*1.1
            return rate
        else:
            rate = base
            return rate
    
class TeamListPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = team_model
        fields = '__all__'

class TeamDetailPageSerializer(TeamListPageSerializer):
    employee = employee_serializer(many=True, read_only=True)
    

# class work_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = work_model
#         fields = ('id','url','name')
