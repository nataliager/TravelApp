from rest_framework import serializers
from travelApp.models.user import User
from travelApp.models.account import Account
from travelApp.serializers.accountSerializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):

    account = AccountSerializer() #se crea clase accountSerializer

    class Meta: #siempre se tiene que llamar Meta
        model = User #modelo
        fields = ['id', 'username', 'password', 'name', 'email','account','isAdmin'] #datos q van json

    #metodos - polimorfismo por herencia de clase padre modelSerializer
    #Trae un diccionario(validated data) info del json
    def create(self, validated_data):
        accountData = validated_data.pop('account')#quita del dic, el account y lo guarda
        userInstance = User.objects.create(**validated_data)#json -->crea un obj de tipo user
        Account.objects.create(user=userInstance, **accountData)#creo obj tipo account
        return userInstance #instancia de user

    def update(self, instance, validated_data):
        validated_data.pop('account')#quita del dic el account        
        return super().update(instance, validated_data)

    def to_representation(self, obj): #conv de obj(base datos) a jeison
        #userInstance = User.objects.get(email=obj.email)
        user = User.objects.get(id=obj.id) #busco obj user --> selected 
        account = Account.objects.get(user=obj.id) #busco obj account -->selected
        
        return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'account': {
                    'id': account.id,
                    'lastChangeDate': account.lastChangeDate,
                    'isActive': account.isActive
                },
                'isAdmin': user.isAdmin,
            }  