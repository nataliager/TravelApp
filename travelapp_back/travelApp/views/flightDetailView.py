from django.conf import settings
from django.http.response import Http404
from travelApp.serializers.flightsSerializer import FlightsSerializer
from travelApp.models.flights import Flights
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FlightDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    #Obtiene la info de un vuelo en especifico por su pk = flightNumber
    def get(self, request, pk,format=None):
        flight = FlightsSerializer.get_object(pk)
        serializer = FlightsSerializer(flight)
        return Response(serializer.data)

    #Actualiza un vuelo segun su pk = flightNumber
    def put(self, request,pk,format=None):
        flight = FlightsSerializer.get_object(pk)
        serializer = FlightsSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Elimina un vuelo de la BD segun su pk = flightNumber
    def delete(self, request,pk,format=None):

        flight = FlightsSerializer.get_object(pk)
        flight.delete()
        return Response({"detail" : "El Vuelo fue eliminado exitosamente"},status=status.HTTP_204_NO_CONTENT)

    
    
    