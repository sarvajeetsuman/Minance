from django.db import models

# Create your models here.

class EmployeeProfile(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        app_label = "employee_details"
        managed = True
    
    def __unicode__(self):
        return employee_id

class EmployeesDevice(models.Model):
    """
    Saves all Employees Device
    """
    employee_id = models.ForeignKey('EmployeeProfile',
        on_delete=models.CASCADE,)
    device_id = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "employee_details"
        managed = True
    
    def __unicode__(self):
        return device_id