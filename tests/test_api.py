import pytest

from django.test.client import Client

from posts.models import Post
from tests.factories import PostFactory, GameFactory

@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_posts_list(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data) == 5

    def test_posts_create(self):
        data = {"title": "test", "text": "testtest"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_games_list(self):
        GameFactory.create_batch(5)
        response = self.client.get("/api/games/")

        assert response.status_code == 200
        assert len(response.data) == 5

    def test_games_create(self):
        data_games = {
            "title": "test",
            "release_data": '2021-08-08',
            "genre": "adventure",
            "platform": "PS5",
            "progress": 78,
            "comment": "test_comment"
        }
        response = self.client.post("/api/games/", data=data_games)
        assert response.status_code == 201

        response = self.client.get("/api/games/")
        assert response.status_code == 200
        assert len(response.data) == 1



