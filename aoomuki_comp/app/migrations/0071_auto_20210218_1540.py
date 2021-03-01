# Generated by Django 3.1.5 on 2021-02-18 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_remove_userprofil_collaborater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborater',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofil',
            name='collaborater',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.collaborater', verbose_name='Collaborateur'),
        ),
    ]
