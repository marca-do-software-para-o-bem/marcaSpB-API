from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Account
        fields = ['cep', 'endereco', 'cnpj']


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False)
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password','account' ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
                first_name=validated_data['first_name'],
            )
            user.set_password(validated_data['password'])
            account_data = validated_data.pop('account')
            account= Account(
                user = user,
                cep= account_data['cep'],
                endereco= account_data['endereco'],
                cnpj= account_data['cnpj']
            )
            user.save()
            account.save()
            return user

    def update(self, instance, validated_data):
        # separa o json do account e sua instancia
        account_data = validated_data.pop('account')
        account = instance.account

        # atualiza os dados da model User
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']

        # atualiza os dados da model Account
        account.cep= account_data.get('cep')
        account.endereco= account_data.get('endereco')
        account.cnpj= account_data.get('cnpj')

        # armazena os dados
        instance.save()
        account.save()

        # retorna o json resultante no metodo PUT
        return instance