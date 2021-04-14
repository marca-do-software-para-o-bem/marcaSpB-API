from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Account

class AccountTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    # faz a requisição e depois compara se foi parar no banco de testes
    def test_post(self):
        data = {
                "username": "Testando",
                "first_name": "Pedro",
                "password": "12345678",
                "email": "testando@emai.com",
                "account": {
                    "cep": "71000000",
                    "endereco": "Minha casa",
                    "cnpj": "033141224"
                }
            }
        request = self.client.post('/usuario/', 
            data,
            format='json')

        user = User.objects.last()
        account = Account.objects.last()
        
        self.assertEquals(data['username'],user.username)
        self.assertEquals(data['first_name'],user.first_name)
        self.assertEquals(data['email'],user.email)
        self.assertEquals(data['account']['cep'],account.cep)
        self.assertEquals(data['account']['endereco'],account.endereco)
        self.assertEquals(data['account']['cnpj'],account.cnpj)








