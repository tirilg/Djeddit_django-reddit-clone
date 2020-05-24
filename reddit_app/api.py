from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .permissions import IsOwner

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,]

class VoteView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    



