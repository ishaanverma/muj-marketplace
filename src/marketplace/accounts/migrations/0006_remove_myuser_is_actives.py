# Generated by Django 2.1.1 on 2018-09-25 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_myuser_is_actives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_actives',
        ),
    ]