from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets,generics
from .models import employee_model, team_model, work_model, leaders_model
from .serializers import employee_serializer, team_serializer, work_serializer,leader_serializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class team_view(viewsets.ModelViewSet):
    queryset = team_model.objects.all()
    serializer_class = Team_serializer

class employeeList(viewsets.ModelViewSet):
    queryset = employee_model.objects.all()
    serializer_class = Employee_serializer

class work_arrange(viewsets.ModelViewSet):
    queryset = work_model.objects.all()
    serializer_class = Work_serializer

class leader(viewsets.ModelViewSet):
    queryset = leaders_model.objects.all()
    serializer_class = Leader_serializer