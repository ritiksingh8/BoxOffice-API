from django.db import models
from django.contrib.auth import get_user_model
from theater.models import Show
from django.urls import reverse
from django.db.models.signals import post_delete
from django.utils import timezone
User = get_user_model()
# Create your models here.


class Booking(models.Model):
    payment_choice = (
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Net Banking', 'Net Banking'),
        ('Wallet', 'Wallet'),
    )
    timestamp         =     models.DateTimeField('%Y-%m-%d %H:%M:%S',default = timezone.now())
    payment_type      =     models.CharField(max_length=11, choices=payment_choice)
    # payment_type      =     models.CharField(max_length=11)
    paid_amount       =     models.DecimalField(max_digits=8, decimal_places=2)
    paid_by           =     models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)
    # def get_absolute_url(self):
    #     return reverse('booking:detail',kwargs={'btid':self.id})
    
    #def get_absolute_url(self):

class Seat(models.Model):
    # seat_choice = (
    #     ('', 'Select'),
    #     ('Silver', 'Silver'),
    #     ('Gold', 'Gold'),
    #     ('Platinum', 'Platinum'),
    # )
    seat_no         =       models.CharField(max_length=3)
    seat_id         =       models.CharField(max_length=4,default='')
    seat_code       =       models.CharField(max_length=4,default='')
    seat_row        =       models.CharField(max_length=4,default='')
    # seat_type       =       models.CharField(max_length=8, choices=seat_choice, blank=False)
    show            =       models.ForeignKey(Show, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('seat_no', 'show')

    def __str__(self):
        return self.seat_no + str(self.show)


class BookedSeat(models.Model):
    seat            =       models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking         =       models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)


def delete_reverse(sender,instance,*args,**kwargs):
    try:
        if instance.seat:
            instance.seat.delete()
    except:
        pass

post_delete.connect(delete_reverse,sender=BookedSeat)