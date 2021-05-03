# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'birthdate', 'gender']
