from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Theater, Show
from movie.serializers import MovieSerializer

class TheaterSerializer(serializers.ModelSerializer):

 	class Meta:
 		model = Theater
 		fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):

	movie = MovieSerializer()
	theater = TheaterSerializer()

	class Meta:
		model = Show
		fields = '__all__'