from django.db import models #models para crear tablas 
from .flights import Flights
from .user import User

import datetime 
from django.utils import timezone

class Bookings(models.Model):

    #Atributos modelo Bookings
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flights,  on_delete=models.CASCADE)
    idUser = models.ForeignKey(User,  on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now())
    