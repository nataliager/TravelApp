from django.conf import settings
from django.http.response import Http404
from travelApp.serializers.bookingSerializer import BookingSerializer
from travelApp.models.bookings import Bookings
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from travelApp.models.user import User

class BookingView(views.APIView):

    permission_classes = (IsAuthenticated,)

    #Obtiene la info de una reserva en especifico por su pk = id
    def get(self, request, pk, format=None):

        token = request.META.get('HTTP_AUTHORIZATION')[7:] #obtener el token 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #traducir token, crea objeto tipo tokenBackend
        valid_data = tokenBackend.decode(token,verify=False)#decoficar token, info token

        userId = valid_data["user_id"]
        booking = BookingSerializer.get_object(pk)
        serializer = BookingSerializer(booking)
        if  userId == serializer.data["idUser"]:
            return Response(serializer.data)
        else: 
            return Response({"detail" : "Reserva no encontrada"},status=status.HTTP_401_UNAUTHORIZED)


    #Elimina una reserva de la BD segun su pk = id
    def delete(self, request, pk, format=None):

        token = request.META.get('HTTP_AUTHORIZATION')[7:] #obtener el token 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #traducir token, crea objeto tipo tokenBackend
        valid_data = tokenBackend.decode(token,verify=False)#decoficar token, info token

        booking = BookingSerializer.get_object(pk)
        booking.delete()
        return Response({"detail" : "La reserva fue eliminada exitosamente"},status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, *args, **kwargs): #solo metodo post

        token = request.META.get('HTTP_AUTHORIZATION')[7:] #obtener el token 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #traducir token, crea objeto tipo tokenBackend
        valid_data = tokenBackend.decode(token,verify=False)#decoficar token, info token

        serializer = BookingSerializer(data=request.data)#creacion obj UserSerializer-> json q llega
        serializer.is_valid(raise_exception=True)#verificar si la info esta correcta
        serializer.save()#guarda en la bd

        #Respuesta: codigo de respuesta CREADO
        return Response({"Estado" : "Reserva Exitosa.... Guarde su Numero de reserva", "NoReserva" : serializer.data["id"]},status=status.HTTP_201_CREATED)
    

   

    
    
    