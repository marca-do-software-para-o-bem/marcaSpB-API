# Generated by Django 3.1.7 on 2021-04-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20210331_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cep',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='endereco',
            field=models.TextField(null=True),
        ),
    ]