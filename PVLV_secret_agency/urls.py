from django.urls import path, include
from rest_framework import routers
from PVLV_secret_agency.api.views import TargetSnippetViewSet

router = routers.DefaultRouter()
router.register('targets', TargetSnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# Create your views here.
