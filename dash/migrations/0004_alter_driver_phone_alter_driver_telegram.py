# Generated by Django 4.0.4 on 2022-05-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_alter_driver_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='driver',
            name='telegram',
            field=models.CharField(blank=True, default=0, max_length=20),
        ),
    ]
