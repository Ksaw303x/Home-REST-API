from django.urls import path, include
from rest_framework import routers
from PVLV_quotes.api.views import PollViewSet


router = routers.DefaultRouter()
router.register('', PollViewSet)

urlpatterns = [
    path('', include(router.urls))
]
