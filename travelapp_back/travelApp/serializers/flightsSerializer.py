from travelApp.models.flights import Flights
from rest_framework import serializers
from django.http.response import Http404

class FlightsSerializer(serializers.ModelSerializer): #heredamos la clase serializer
    
    class Meta:
        model = Flights #modelo account 
        fields = ['flightNumber', 'departureDate', 'returnDate','origin','destination','airline','weight', 'price'] #campos a serializar
        #no inlcuimos user porque es otra clase y se pone en el userSerializer

    #Valida si un vuelo existe en la base de datos
    def get_object(pk):
        try:
            return Flights.objects.get(pk=pk)
        except Flights.DoesNotExist:
            raise Http404
