from rest_framework import routers
from assign import views

router = routers.DefaultRouter()
router.register('employee',views.EmployeeViewset)



