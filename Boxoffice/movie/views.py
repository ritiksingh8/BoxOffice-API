from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MovieSerializer, SearchMovieSerializer
from theater.serializers import TheaterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Movie
from theater.models import Show
# Create your views here.



class ManageMovieAPIView(APIView):

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

class ManageMovieDetailAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	def get_object(self,id):

		try:
			return Movie.objects.get(id=id)

		except MovieDoesNotExist as e:
			return Response({'error':'Given Question object not found'},status=400)

	def get(self, request,id):
		movie = self.get_object(id=id)
		serailizer = MovieSerializer(movie)
		return Response(serailizer.data, status=200)

class ManageMovieTheaterDetailAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	def get_object(self,id):

		try:
			return Movie.objects.get(id=id)

		except MovieDoesNotExist as e:
			return Response({'error':'Given Question object not found'},status=400)

	def get(self, request,id):
		movie = self.get_object(id=id)
		shows = Show.objects.filter(movie=movie)
		theaters = [show.theater for show in shows]
		serailizer = TheaterSerializer(theaters,many=True)
		return Response(serailizer.data, status=200)

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