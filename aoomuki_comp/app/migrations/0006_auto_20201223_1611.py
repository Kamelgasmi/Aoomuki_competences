# Generated by Django 2.1 on 2020-12-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201223_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
    ]
