# Generated by Django 3.1.5 on 2021-02-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_auto_20210203_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofcompetence',
            name='ListInterest',
            field=models.CharField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default='0', max_length=10, unique=True, verbose_name='valeur'),
        ),
        migrations.AlterField(
            model_name='listofcompetence',
            name='ListLevel',
            field=models.CharField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default='0', max_length=10, unique=True, verbose_name='valeur'),
        ),
    ]