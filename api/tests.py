from rest_framework.test import APIClient

from django.test import TestCase

from .models import Post, Tag, User, Vote


class TestCasePost(TestCase):
    def setUp(self) -> None:
        self.guest_client = APIClient()

        self.user = User.objects.create_user(username="my_user", password="some_pass")
        self.client = APIClient()
        self.client.force_login(user=self.user)

        self.admin = User.objects.create_user(
            username="my_admin", password="somme_pass", is_staff=True
        )
        self.admin_client = APIClient()
        self.admin_client.force_login(user=self.admin)
        self.post = Post.objects.create(
            title="Test Post", body="This is a test post.", author=self.user
        )

    def test_viewing_posts(self):
        response = self.client.get("/api/v1/posts/")

        assert response.status_code == 200, response.data

    # Added permission to the PostViewSet

    def test_create_post(self):
        response = self.client.post("api/v1/posts")

        assert response.status_code == 404, response.data

    def test_author_can_update_post(self):
        response = self.client.patch(
            f"/api/v1/posts/{self.post.id}/", {"title": "Updated Test Post"}
        )
        assert response.status_code == 200, response.data

    def test_admin_can_update_post(self):
        response = self.admin_client.patch(
            f"/api/v1/posts/{self.post.id}/", {"title": "Updated Test Post"}
        )
        assert response.status_code == 200, response.data

    def test_other_user_cannot_update_post(self):
        other_user = User.objects.create_user(username="other", password="otherpass")
        other_client = APIClient()
        other_client.force_login(user=other_user)

        response = other_client.patch(
            f"/api/v1/posts/{self.post.id}/", {"title": "Updated Test Post"}
        )
        assert response.status_code == 403, response.data

    def test_author_can_delete_post(self):
        response = self.client.delete(f"/api/v1/posts/{self.post.id}/")
        assert response.status_code == 204, response.data

    def test_admin_can_delete_post(self):
        response = self.admin_client.delete(f"/api/v1/posts/{self.post.id}/")
        assert response.status_code == 204, response.data

    def test_other_user_cannot_delete_post(self):
        other_user = User.objects.create_user(username="other", password="otherpass")
        other_client = APIClient()
        other_client.force_login(user=other_user)

        response = other_client.delete(f"/api/v1/posts/{self.post.id}/")
        assert response.status_code == 403, response.data


class TestCaseTag(TestCase):
    def setUp(self) -> None:
        self.guest_client = APIClient()

        self.user = User.objects.create_user(username="my_user", password="some_pass")
        self.client = APIClient()
        self.client.force_login(user=self.user)

        self.tag = Tag.objects.create(
            title="Test Tag",
        )

    def test_see_tag_anyone(self):
        response = self.guest_client.get("/api/v1/tags/")

        assert response.status_code == 200, response.data

    def test_not_create_tag_if_not_is_authenticated(self):
        response = self.guest_client.post("/api/v1/tags/")

        assert response.status_code == 401, response.data

    def test_not_admin_can_not_update_tag(self):
        response = self.client.patch(
            f"/api/v1/tags/{self.tag.id}/", {"title": "Updated Test Tag"}
        )
        assert response.status_code == 403, response.data

    def test_not_admin_can_not_delete_tag(self):
        response = self.client.delete(f"/api/v1/tags/{self.tag.id}/")
        assert response.status_code == 403, response.data


class TestCaseVote(TestCase):
    def setUp(self) -> None:
        self.guest_client = APIClient()

        self.user = User.objects.create_user(username="my_user", password="some_pass")
        self.client = APIClient()
        self.client.force_login(user=self.user)

        self.admin = User.objects.create_user(
            username="my_admin", password="somme_pass", is_staff=True
        )
        self.admin_client = APIClient()
        self.admin_client.force_login(user=self.admin)

        self.post = Post.objects.create(
            title="Test Post", body="This is a test post.", author=self.user
        )

        self.vote = Vote.objects.create(
            user=self.user,
            post=self.post,
            up=True,
        )

    def test_see_vote_anyone(self):
        response = self.guest_client.get("/api/v1/votes/")

        assert response.status_code == 200, response.data

    def test_not_create_vote_if_not_is_authenticated(self):
        response = self.guest_client.post("/api/v1/votes/")

        assert response.status_code == 401, response.data

    def test_not_update_vote_if_not_author(self):
        other_user = User.objects.create_user(username="other", password="otherpass")
        other_client = APIClient()
        other_client.force_login(user=other_user)

        response = other_client.patch(
            f"/api/v1/votes/{self.vote.id}/", {"post_id": "5", "up": True}
        )
        assert response.status_code == 403, response.data

    def test_author_can_update_vote(self):
        response = self.client.patch(f"/api/v1/votes/{self.vote.id}/", {"up": False})
        assert response.status_code == 200, response.data

    def test_author_can_delete_vote(self):
        response = self.client.delete(f"/api/v1/votes/{self.vote.id}/")
        assert response.status_code == 204, response.data
