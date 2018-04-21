from django.db import models

# Create your models here.

class EmployeeProfile(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)

    class Meta:
        app_label = "employee_details"
        managed = True
    
    def __unicode__(self):
        return employee_id

