from django.conf import settings
from django.db.models.query import QuerySet
from travelApp.serializers.flightsSerializer import FlightsSerializer
from travelApp.models.flights import Flights
from travelApp.serializers.flightsSerializer import FlightsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class FlightApiView(APIView):

    #Obtiene todos los vuelos de la BD
    def get(self, request, *args, **kwargs):
        flights = Flights.objects.all()
        serializer = FlightsSerializer(flights, many=True)
        return Response(serializer.data)

