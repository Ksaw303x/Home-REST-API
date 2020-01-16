from django.urls import path, include
from PVLV_services.api.views import datetime_now, server_ip


urlpatterns = [
    path('datetime-now', datetime_now),
    path('server-public-ip', server_ip),
]
