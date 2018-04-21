from django.conf.urls import url, include
from employee_details import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee-profile', views.EmployeeProfileViewSet)
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'send-sms-to-employee', views.send_sms_to_employee, name="send_sms_to_employee"),
]