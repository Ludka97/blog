import random

import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User

from posts.models import Post
from games.models import Game


class PostFactory(DjangoModelFactory):
   class Meta:
       model = Post

   title = factory.Faker("word")
   text = factory.Faker("sentence")


class GameFactory(DjangoModelFactory):
   class Meta:
       model = Game

   title = factory.Faker("word")
   release_data = factory.Faker("date")
   genre = factory.Faker("sentence")
   platform = factory.Faker("word")
   progress = random.randrange(start=0, stop=100)
   comment = factory.Faker("sentence")


class UserFactory(DjangoModelFactory):
   class Meta:
       model = User

   username = factory.Faker("word")
   email= factory.Faker("email")
