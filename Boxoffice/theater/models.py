from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from movie.models import Movie
from django.urls.base import reverse
User = get_user_model()

class Theater(models.Model):
    city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad')
    )
    name            =   models.CharField(max_length=50,null=False)
    city            =   models.CharField(max_length=9,choices=city_choice,null=False)
    # city            =   models.CharField(max_length=9,null=False)
    address         =   models.CharField(max_length=100)
    no_of_screen    =   models.IntegerField()
    
    def __str__(self):
        return self.name+"-"+self.address+"-"+self.city
    
    # def get_absolute_url(self):
    #     return reverse('theatre:detail',kwargs={'theatre_id':self.pk})
    
class Show(models.Model):
    movie       =    models.ForeignKey(Movie,on_delete=models.CASCADE)
    theater     =    models.ForeignKey(Theater,on_delete=models.CASCADE)
    screen      =    models.IntegerField()
    date        =    models.DateField()
    time        =    models.TimeField()
    
    def __str__(self):
        return str(self.movie)+"-"+str(self.theater)+"-"+str(self.date)+"-"+str(self.time)