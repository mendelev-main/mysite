from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "url", "username", "email", "is_staff"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ["title", "body", "author_id", "pub_date", "url"]


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vote
        fields = ["post", "user", "up", "url"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ["title", "url"]
