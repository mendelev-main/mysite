from rest_framework import filters, pagination, viewsets

from . import models, serializers


class PostAndTagPagination(pagination.LimitOffsetPagination):
    default_limit = 3


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = PostAndTagPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["pub_date"]
    search_fields = ["title", "body"]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    pagination_class = PostAndTagPagination
