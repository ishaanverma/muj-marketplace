# Generated by Django 2.1.1 on 2018-09-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_myuser_is_actives'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
