from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from .models import Post
from .serializers import PostModelSerializer

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

