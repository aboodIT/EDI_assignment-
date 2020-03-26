from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from assign import views

# router = routers.DefaultRouter()
# router.register('employeelist',views.employeelist)
# #router.register('employeedetail',views.EmployeeDetail)
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# #urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns = [
    path('teams/', views.team_view, name='team_view'),
    path('teams/<int:pk>/', views.team_detail_view, name='team_detail_view'),
    path('teams/<int:pk>/employees', views.employee_view, name='employees_view'),
    path('employees/',views.employee_list_view, name='employee_list'),
    path('employees/<int:pk>/',views.employee_detail_view, name='employee_detail'),
    path('leaders/',views.leader_view, name='leader'),
]
