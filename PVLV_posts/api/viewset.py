from PVLV_posts.models import Post
from PVLV_posts.api.serializers import PostSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class PostSnippetViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date_creation').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
