from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user','cep','endereco','cnpj']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        account= Account(
            user = validated_data['user'],
            cep= validated_data['cep'],
            endereco= validated_data['endereco'],
            cnpj= validated_data['cnpj']
        )
        return user

    def update(self, validated_data):
        pass