from rest_framework import serializers
from PVLV_posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'date_creation',)
