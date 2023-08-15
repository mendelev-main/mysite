from rest_framework import routers

from django.urls import include, path

from . import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("posts", views.PostViewSet)
router.register("votes", views.VoteViewSet)
router.register("tags", views.TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("authtoken/", include("djoser.urls.authtoken")),
    path("authjwt/", include("djoser.urls.jwt")),
]
