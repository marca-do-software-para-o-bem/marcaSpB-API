from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9, null=False)
    endereco =  models.TextField(null=False)
    cnpj = models.CharField(max_length=14, null=True)
