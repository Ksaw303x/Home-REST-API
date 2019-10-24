from PVLV_posts.models import Post
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'date_creation',
        )
