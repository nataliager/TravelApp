from django.db import models #models para crear tablas 

class Flights(models.Model):

    #Atributos modelo Flights
    flightNumber = models.CharField(primary_key=True,max_length = 10)#numero de vuelo
    departureDate = models.DateTimeField() #fecha de ida
    returnDate = models.DateTimeField() #fecha de regreso
    origin = models.CharField( max_length = 15)
    destination = models.CharField( max_length = 15)
    airline = models.CharField( max_length = 10)
    weight = models.IntegerField()
    price = models.IntegerField()
    