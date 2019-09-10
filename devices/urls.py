from django.urls import path
from devices.views import TDBaseServerAPI

urlpatterns = [
    path('tdbase/tag/', TDBaseServerAPI.as_view(), name='api-stampings'),
]
