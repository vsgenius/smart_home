# Generated by Django 4.0.3 on 2022-04-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='measurement',
            field=models.ManyToManyField(related_name='sensor', to='measurement.measurement'),
        ),
    ]
