from django.urls import path, include
from rest_framework import routers
from PVLV_posts.api.views import PostSnippetViewSet


router = routers.DefaultRouter()
router.register('', PostSnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]