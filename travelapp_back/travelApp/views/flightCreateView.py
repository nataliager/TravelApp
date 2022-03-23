#creacion del usuario
from rest_framework import status, views
from rest_framework.response import Response
from travelApp.serializers.flightsSerializer import FlightsSerializer

class FlightCreateView(views.APIView):

    #Crea un vuelo en la BD 
    def post(self, request, *args, **kwargs): #solo metodo post

        serializer = FlightsSerializer(data=request.data)#creacion obj UserSerializer-> json q llega
        serializer.is_valid(raise_exception=True)#verificar si la info esta correcta
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"detail" : "El Vuelo fue agregado exitosamente"})