from django import shortcuts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic

from .models import Post, Vote, Tag


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
    fields = ["title", "body", 'tag', ]
    template_name = "blog/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def upvote(request, pk: int):
    return _vote(request=request, pk=pk, up=True)


def downvote(request, pk: int):
    return _vote(request=request, pk=pk, up=False)


def _vote(request, pk: int, up: bool):
    post = shortcuts.get_object_or_404(Post, pk=pk)
    Vote.objects.update_or_create(post=post, user=request.user, defaults={'up': up})
    return shortcuts.redirect('blog:detail', pk=pk)


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = ["title", ]
    template_name = "blog/create_tag.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

