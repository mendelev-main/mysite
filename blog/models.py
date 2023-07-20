from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})


# auto_now_add=True - don't work
