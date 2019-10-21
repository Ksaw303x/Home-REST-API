from rest_framework import viewsets
from PVLV_posts.models import Post
from .serializers import PostSerializer


class PostSnippetViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
