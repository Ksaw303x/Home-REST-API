from django.urls import path, include
from rest_framework import routers
from PVLV_quotes.api.views import QuotesSnippetViewSet


router = routers.DefaultRouter()
router.register('v1/quote', QuotesSnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
