from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name','description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature','created_at']


class SensorPkSerializer(serializers.ModelSerializer):
    measurement = serializers.StringRelatedField(many=True)
    class Meta:
        model = Sensor
        fields = ['id','name','description', 'measurement']


# class SensorMeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SensorMeasurement
#         fields = ['sensor', 'measurement']