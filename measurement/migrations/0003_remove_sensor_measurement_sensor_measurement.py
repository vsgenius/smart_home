# Generated by Django 4.0.3 on 2022-04-11 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_sensor_measurement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurement',
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='measurement.measurement'),
            preserve_default=False,
        ),
    ]
