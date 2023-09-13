from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response

from posts.models import Post, Tag
from .serializers import PostSerializer, TagSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()[:5]
    serializer_class = PostSerializer

class SinglePostAPIView(RetrieveAPIView):
    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            qs = Post.objects.filter(slug__iexact=slug) 
            if qs.exists():
                obj = qs
            else:
                obj = []
        return obj
    serializer_class = PostSerializer
    lookup_field = 'slug'

class TagAPIView(ListAPIView):
    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            qs = Post.objects.filter(tags__tag__icontains=slug)
            if qs.exists():
                return qs
            else: 
                return []
    serializer_class = PostSerializer

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer