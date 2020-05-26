from rest_framework import serializers
from .models import Vote, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'text', 'votes', 'created_at')
        model = Post
        """ depth = 1 """

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('vote', 'post', 'user')
        model = Vote