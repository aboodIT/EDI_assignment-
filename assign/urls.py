from django.urls import path,include
from assign import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employeelist',views.EmployeeList)
#router.register('employeedetail',views.EmployeeDetail)
urlpatterns = [
    path('', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)