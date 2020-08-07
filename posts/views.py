from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from django.db import IntegrityError
from posts.models import Post
from posts.serializers import PostSerializer
from posts.error_logger import LOGGER


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Upvote(APIView):
    def get_object(self, pk):
        return Post.objects.get(pk=pk)

    def patch(self, request, pk):
        post = self.get_object(pk)
        post.upvote()
        try:
            post.save()
            return HttpResponse(status=201)
        except IntegrityError as e:
            LOGGER.error(e)
            return HttpResponse(status=500)
