from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorRetriveView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorRetriveView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    # path('RetrieveUpdateAPIView/',RetrieveUpdateAPIView),
    # path('ListCreateAPIView/',ListCreateAPIView),
]
