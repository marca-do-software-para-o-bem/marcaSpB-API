from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model: Account
        fields = ['cep', 'endereco', 'cnpj']


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=True)
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
        user.save()
        account_data = validated_data.pop['account']
        account= Account(
            user = user,
            cep= account_data['cep'],
            endereco= account_data['endereco'],
            cnpj= account_data['cnpj']
        )
        return user

    def update(self, validated_data):
        pass