from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorPkSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor(name=request.data['name'],description=request.data['description']).save()
        return Response({'status':'OK'})


class SensorRetriveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorPkSerializer

    def patch(self,request,pk):
        Sensor.objects.filter(id=pk).update(description=request.data['description'])
        return Response({'status':'OK'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        Measurement(sensor_id=request.data['sensor'],temperature=request.data['temperature']).save()
        return Response({'status':'OK'})
