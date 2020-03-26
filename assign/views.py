from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets,generics
from .models import employee_model, team_model, work_model, leaders_model
from .serializers import employee_serializer, TeamDetailPageSerializer, TeamListPageSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Team Details 
@api_view(['GET', 'POST'])
def team_view(request):
    if request.method == 'GET':
        team = team_model.objects.all()
        serializer = TeamListPageSerializer(team, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TeamListPageSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            serializer = TeamListPageSerializer(team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH', 'DELETE'])
def team_detail_view(request, pk):
    try:
        team = team_model.objects.get(pk=pk)
    except team_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TeamDetailPageSerializer(team)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = TeamDetailPageSerializer(team, data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            print(team)
            return Response(TeamDetailPageSerializer(team).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        team.delete()
        return Response("Team dismantled", status=status.HTTP_204_NO_CONTENT)


#Employee details 
@api_view(["GET"])
def employee_list_view(request):
    employees = employee_model.objects.all()
    serializer = employee_serializer(employees,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def employee_view(request, pk=None):
    try:
        team = team_model.objects.get(pk=pk)
    except team_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        employees = employee_model.objects.filter(team=team)
        print(employees)
        serializer = employee_serializer(employees,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = employee_serializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save(team = team)
            print(employee)
            return Response(employee_serializer(employee).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def employee_detail_view(request, pk=None):
    try:
        employee = employee_model.objects.get(pk=pk)
    except team_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = employee_serializer(employee)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = employee_serializer(employee, data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(employee_serializer(employee).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response("Employee removed", status=status.HTTP_204_NO_CONTENT)


#Leader details
@api_view(["GET"])
def leader_view(request):
    if request.method == 'GET':
        leader = employee_model.objects.filter(leader=True)
        serializer = employee_serializer(leader, many=True)
        return Response(serializer.data)


# class team_view(viewsets.ModelViewSet):
#     queryset = team_model.objects.all()
#     serializer_class = team_serializer

# class employeelist(viewsets.ModelViewSet):
#     queryset = employee_model.objects.all()
#     serializer_class = employee_serializer

# class work_arrange(viewsets.ModelViewSet):
#     queryset = work_model.objects.all()
#     serializer_class = work_serializer


# class leader(viewsets.ModelViewSet):
#     queryset = leaders_model.objects.all()
#     serializer_class = leader_serializer