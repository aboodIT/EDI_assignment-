from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets,generics
from .models import Employee_model
from .serializers import Employee_serializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class EmployeeList(viewsets.ViewSet):
    queryset = Employee_model.objects.all()
    serializer_class = Employee_serializer

class EmployeeDetail(viewsets.ViewSet):
    queryset = Employee_model.objects.all()
    serializer_class = Employee_serializer
