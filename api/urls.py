from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("posts", views.PostViewSet)
router.register("votes", views.VoteViewSet)
router.register("tags", views.TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
