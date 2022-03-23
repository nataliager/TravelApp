from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from travelApp.models.account import Account
from travelApp.models.user import User
from travelApp.serializers.userSerializer import UserSerializer

class UserView(views.APIView):

    permission_classes = (IsAuthenticated,)    

    #Permite al usuario logueado ver sus datos
    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False) 
        
        serializer = UserSerializer()
        u = User(id = valid_data["user_id"])
        result = serializer.to_representation(u)

        return Response(result, status=status.HTTP_200_OK)

    #Permite al usuario logueado actualizar sus datos   
    def put(self, request, *args, **kwargs):

        #Decodificaciond del token
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        request.data["id"] = valid_data["user_id"] #obtener id del token
        user = User(id = valid_data["user_id"])#crear un obj de tipo user

        #Actualizar el usuario autenticado
        serializer = UserSerializer(user, data=request.data)        
        serializer.is_valid(raise_exception=True)#valida      
        updatedUser = serializer.save()#guarda
        result = serializer.to_representation(updatedUser) #convierte a json

        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        request.data["id"] = valid_data["user_id"] #obtener id del token
        u = User(id = valid_data["user_id"])#crear un obj de tipo user  
        u.delete()

        return Response({"detail" : "El usuario fue eliminado exitosamente"},status=status.HTTP_204_NO_CONTENT)
        
       

       

       