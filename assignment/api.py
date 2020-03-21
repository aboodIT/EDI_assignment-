from rest_framework import routers
from assign import views

router = routers.DefaultRouter()
router.register('employee',views.EmployeeList)
router.register('team', views.Team_view)
router.register('arrangement',views.Work_arrange)
router.register('leaders',views.Leader)



