from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyPagination
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title"]
    search_fields = ["title", "contents"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
