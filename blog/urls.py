from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create/", views.PostCreateView.as_view(), name="create_post"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
