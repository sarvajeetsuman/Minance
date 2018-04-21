from rest_framework import serializers
from employee_details import models

class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
    Serializer used with EmployeeProfile Model
    """

    class Meta:
        model = models.EmployeeProfile
        fields = ('employee_id', 'first_name', 'last_name', 'device_id')
        