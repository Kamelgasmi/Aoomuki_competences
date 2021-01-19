# Generated by Django 2.1 on 2021-01-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_collaborater_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competence',
            name='field',
        ),
        migrations.AddField(
            model_name='field',
            name='competence',
            field=models.ManyToManyField(blank=True, related_name='field', to='app.Competence'),
        ),
    ]
