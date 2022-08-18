from django.conf import settings
from django.db import models


class Game(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="games",
        blank=True,
        null=True
    )

    title = models.CharField(max_length=50)
    release_data = models.DateField()
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=20)
    progress = models.IntegerField()
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Post: {self.title}"
