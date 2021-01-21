# Generated by Django 2.1 on 2021-01-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20210121_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10, unique=True, verbose_name='valeur')),
                ('commentary', models.CharField(max_length=250, verbose_name='commentaire')),
            ],
            options={
                'verbose_name': 'Liste des intérêts',
            },
        ),
        migrations.CreateModel(
            name='ListLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10, unique=True, verbose_name='valeur')),
                ('commentary', models.CharField(max_length=250, verbose_name='commentaire')),
            ],
            options={
                'verbose_name': 'Liste des niveaux',
            },
        ),
        migrations.RemoveField(
            model_name='collaborater',
            name='competences',
        ),
        migrations.RemoveField(
            model_name='listofcompetence',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='listofcompetence',
            name='level',
        ),
        migrations.AddField(
            model_name='listofcompetence',
            name='ListInterest',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListInterest'),
        ),
        migrations.AddField(
            model_name='listofcompetence',
            name='ListLevel',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListLevel'),
        ),
    ]
