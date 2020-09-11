from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Theater

class TheaterSerializer(serializers.ModelSerializer):

 	class Meta:
 		model = Theater
 		fields = '__all__'