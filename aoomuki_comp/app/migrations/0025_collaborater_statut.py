# Generated by Django 2.1 on 2021-01-15 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20210115_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborater',
            name='statut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Statut'),
        ),
    ]
