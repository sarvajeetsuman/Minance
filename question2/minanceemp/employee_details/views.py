from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employee_details import serializers
from employee_details import models
import minance_sms
# Create your views here.



class EmployeeProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating reading updating and deleting employee profiles
    """

    serializer_class = serializers.EmployeeProfileSerializer
    queryset = models.EmployeeProfile.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'employee_id', )

@api_view(['POST'])
def send_sms_to_employee(request):
    """
    To send the message
    """
    number = request.POST["mobile"]
    message = request.POST["message"]
    try:
        minance_sms.solutions_infiniti.send_sms(number, message)
    except e:
        return Response({"status":"Success, Message sending Failed"}, status.HTTP_400_BAD_REQUEST)
    return Response({"status":"Success, Message Sent"}, status.HTTP_200_OK)