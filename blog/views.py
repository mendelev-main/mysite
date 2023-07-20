from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "blog/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
