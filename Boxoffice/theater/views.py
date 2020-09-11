from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TheaterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Theater
# Create your views here.



class TheaterAPIView(APIView):

	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	def get(self, request):
		theaters = Theater.objects.all()
		serailizer = TheaterSerializer(theaters, many=True)
		return Response(serailizer.data, status=200)

	def post(self, request):
		data = request.data
		serializer = TheaterSerializer(data=data)
		if serializer.is_valid():
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)