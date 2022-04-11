from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s: %s' % (self.temperature,self.created_at)


