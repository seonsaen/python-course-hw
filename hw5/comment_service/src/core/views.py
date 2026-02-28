from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def popular(self, request):
        popular_posts = Post.objects.annotate(
            total_comments=Count('comments')
        ).order_by('-total_comments')

        serializer = self.get_serializer(popular_posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer