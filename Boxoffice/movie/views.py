from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MovieSerializer, SearchMovieSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Movie
# Create your views here.



class MovieAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	def get(self, request):
		movies = Movie.objects.all()
		serailizer = MovieSerializer(movies, many=True)
		return Response(serailizer.data, status=200)

	def post(self, request):
		data = request.data
		serializer = MovieSerializer(data=data)
		if serializer.is_valid():
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)

class SearchMovieAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	# def get(self, request):
	# 	movies = Movie.objects.all()
	# 	serailizer = MovieSerializer(movies, many=True)
	# 	return Response(serailizer.data, status=200)

	def post(self, request):
		data = request.data
		serializer = SearchMovieSerializer(data=data)
		if serializer.is_valid():
			movies = Movie.objects.search(serializer.data['query'])
			m_serializer = MovieSerializer(movies,many=True)
			return Response(m_serializer.data, status=201)
		return Response(serializer.errors, status=400)