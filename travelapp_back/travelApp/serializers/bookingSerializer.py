from travelApp.models.bookings import Bookings
from rest_framework import serializers
from travelApp.models.user import User
from travelApp.models.flights import Flights
from django.http.response import Http404


class BookingSerializer(serializers.ModelSerializer): #heredamos la clase serializer
    
    class Meta:
        model = Bookings #modelo account 
        fields = ['id','flight','idUser','date'] #campos a serializar

        def to_representation(self, obj): #conv de obj(base datos) a jeison

            booking = Bookings.objects.get(id=obj.id)
            user = User.objects.get(id=obj.id) #busco obj user --> selected 
            flights = Flights.objects.get(flightNumber=obj.flight)
        
            return {
                        'id': booking.id,
                        'flight': flights.flightNumber,
                        'idUser':  user.id,
                        'date' :booking.date
                    }  
    #Valida si la reserva esta en la BD
    def get_object(pk):
        try:
            return Bookings.objects.get(pk=pk)
        except Bookings.DoesNotExist:
            raise Http404