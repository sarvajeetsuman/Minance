from rest_framework import serializers
from employee_details import models

class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
    Serializer used with EmployeeProfile Model
    """

    class Meta:
        model = models.EmployeeProfile
        fields = ('employee_id', 'first_name', 'last_name')
        

class EmployeeDeviceSerializer(serializers.ModelSerializer):
    """
    Serializer used with EmployeeDevice Model
    """

    class Meta:
        model = models.EmployeesDevice
        fields = ('employee_id', 'device_id')