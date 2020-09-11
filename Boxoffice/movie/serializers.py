from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

	class Meta:

		model = Movie
		fields = ['name','cast','director','language','run_length','certificate','popularity_index','trailer','image']

class SearchMovieSerializer(serializers.Serializer):
    query = serializers.CharField()

    def validate(self, data):
        query = data.get("query", "").strip()
     
        if query == '':
            user = authenticate(username=username, password=password)
            msg = "Enter some valid search query."
            raise exceptions.ValidationError(msg)

        return data