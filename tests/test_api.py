import faker
import pytest
from django.contrib.auth.models import User
from django.test.client import Client

from tests.factories import (
    GameFactory,
    PostFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.fake = faker.Faker()
        self.user = User.objects.create(username="test", email="test")
        self.user = UserFactory()

    def test_register(self):
        data = {
            "email": self.fake.email(),
            "password": self.fake.md5(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }

        response = self.client.post("/api/register/", data=data)
        assert response.status_code == 201

        response = self.client.post("/api/login/", data=data)
        assert response.status_code == 200

    def test_posts_list(self):
        self.client.force_login(self.user)

        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data["results"]) == 5

    def test_posts_create(self):
        self.client.force_login(self.user)

        data = {"title": "test", "text": "testtest"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert "image" in response.data["results"][0]

    def test_games_list(self):
        GameFactory.create_batch(5)
        response = self.client.get("/api/games/")

        assert response.status_code == 200
        assert len(response.data["results"]) == 5

    def test_games_create(self):
        data_games = {
            "title": "test",
            "release_data": "2021-08-08",
            "genre": "adventure",
            "platform": "PS5",
            "progress": 78,
            "comment": "test_comment",
        }
        response = self.client.post("/api/games/", data=data_games)
        assert response.status_code == 201

        response = self.client.get("/api/games/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
