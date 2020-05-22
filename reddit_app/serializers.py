from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('vote', 'post_id', 'user_id')
        model = Vote