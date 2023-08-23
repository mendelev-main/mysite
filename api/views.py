from rest_framework import filters, pagination, permissions, viewsets
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from . import models, serializers
from .permissions import IsAuthor, IsAuthorOrAdmin


class PostAndTagPagination(pagination.LimitOffsetPagination):
    default_limit = 3


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [
        permissions.IsAdminUser | permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = PostAndTagPagination

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["pub_date"]
    search_fields = ["title", "body"]

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            # Apply the IsAuthorOrAdmin permission class for update and delete actions
            permission_classes = [IsAuthorOrAdmin]
        elif self.action == "create":
            # Apply the IsAuthenticated permission class for the create action
            permission_classes = [IsAuthenticated]
        else:
            # Apply the DjangoModelPermissionsOrAnonReadOnly permission class for other actions
            permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

        # Instantiate the permission classes and return them
        return [permission() for permission in permission_classes]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            # Apply the IsAdminUser permission class for update and delete actions
            permission_classes = [IsAuthor]
        elif self.action == "create":
            # Apply the IsAuthenticated permission class for the create action
            permission_classes = [IsAuthenticated]
        else:
            # Apply the DjangoModelPermissionsOrAnonReadOnly permission class for other actions
            permission_classes = [IsAuthenticatedOrReadOnly]

        # Instantiate the permission classes and return them
        return [permission() for permission in permission_classes]


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    pagination_class = PostAndTagPagination

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            # Apply the IsAdminUser permission class for update and delete actions
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            # Apply the IsAuthenticated permission class for the create action
            permission_classes = [IsAuthenticated]
        else:
            # Apply the DjangoModelPermissionsOrAnonReadOnly permission class for other actions
            permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

        # Instantiate the permission classes and return them
        return [permission() for permission in permission_classes]
