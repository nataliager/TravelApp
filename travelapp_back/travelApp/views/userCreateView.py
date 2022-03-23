#creacion del usuario
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from travelApp.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from travelApp.models.user import User

class UserCreateView(views.APIView):

   
    def post(self, request, *args, **kwargs): #solo metodo post

        serializer = UserSerializer(data=request.data)#creacion obj UserSerializer-> json q llega
        serializer.is_valid(raise_exception=True)#verificar si la info esta correcta
        serializer.save()#guarda en la bd

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}#info token dentro del JWT
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)#Serializamos el token en JWT valido
        tokenSerializer.is_valid(raise_exception=True)#verifica que todo este bien
        
        #Respuesta valor del token y un codigo de respuesta
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

   