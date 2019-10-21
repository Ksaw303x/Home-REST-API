from django.urls import path, include
from rest_framework import routers
from PVLV_posts.api.viewset import PostSnippetViewSet


router = routers.DefaultRouter()
router.register('posts', PostSnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]