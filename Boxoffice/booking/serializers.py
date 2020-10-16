from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework import exceptions
from .models import Booking, Seat,BookedSeat
from movie.models import Movie
from theater.models import Theater,Show
# from .models import Post

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.Serializer):
    payment_type = serializers.CharField()
    paid_amount = serializers.DecimalField(max_digits=8,decimal_places=2)
    paid_by = serializers.CharField()

    seat_no = serializers.CharField()
    seat_id = serializers.CharField()
    seat_code = serializers.CharField()
    seat_row = serializers.CharField()

    # movie_name = serializers.CharField()
    # theater_name = serializers.CharField()

    show_id = serializers.CharField()


    def validate(self, data):
        payment_type = data.get("payment_type", "")
        paid_amount = data.get("paid_amount", "")
        paid_by = data.get("paid_by", "")

        seat_no = data.get("seat_no", "")
        seat_id = data.get("seat_id", "")
        seat_code = data.get("seat_code", "")
        seat_row = data.get("seat_row", "")

        # movie_name = data.get("movie_name", "")
        # theater_name = data.get("theater_name", "")

        show_id = data.get("show_id","")

        if payment_type and paid_amount and paid_by and seat_no and seat_id and seat_code and seat_row and show_id:

            user_obj = User.objects.filter(username=paid_by).first()

            if user_obj is None:

                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)

            
            booking_obj = Booking.objects.create(payment_type=payment_type,paid_amount=paid_amount,paid_by=user_obj)
            booking_obj.save()

            # movie_obj = Movie.objects.filter(name=movie_name).first()
            # theater_obj = Theater_obj.filter(name=theater_name).first()

            # if movie_obj is None or theater_obj is None:

            #     msg = "Unable to login with given credentials."
            #     raise exceptions.ValidationError(msg)

            # show_obj = Show.objects.filter(movie=movie_obj,theater=theater_obj).first()

            show_obj = Show.objects.filter(id=show_id).first()

            if show_obj is None:

                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)

            seat_obj = Seat.objects.create(show=show_obj,seat_no=seat_no,seat_id=seat_id,seat_code=seat_code,seat_row=seat_row)
            seat_obj.save()

            if seat_obj is None:

                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)

            booked_seat_obj = BookedSeat.objects.create(seat=seat_obj,booking=booking_obj)
            booked_seat_obj.save()

            data["booked_seat_obj"] = booked_seat_obj


        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data