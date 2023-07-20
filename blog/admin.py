from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ["title", "body", "pub_date"]


admin.site.register(Post)
