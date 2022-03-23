from travelApp.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer): #heredamos la clase serialize
    
    class Meta:
        model = Account #modelo account 
        fields = ['lastChangeDate', 'isActive'] #campos a serializar
        #no inlcuimos user porque es otra clase y se pone en el userSerializer