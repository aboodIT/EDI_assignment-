from django.urls import path
from assign import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)