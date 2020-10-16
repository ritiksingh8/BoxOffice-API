from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView
from .serializers import BookingSerializer, SeatSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from theater.models import Show
from .models import Seat

class BookingView(GenericAPIView):
    serializer_class = BookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    
    def post(self, request,id,pk):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booked_seat_obj = serializer.validated_data["booked_seat_obj"]
        return Response({"status": 'True' }, status=200)

class SeatView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes =[IsAuthenticated]

	def get_object(self,pk):

		try:
			return Show.objects.get(id=pk)

		except ShowDoesNotExist as e:
			return Response({'error':'Given Show object not found'},status=400)

	def get(self, request,id,pk):
		show = self.get_object(pk=pk)
		seats = Seat.objects.filter(show=show)
		serailizer = SeatSerializer(seats,many=True)
		return Response(serailizer.data, status=200)