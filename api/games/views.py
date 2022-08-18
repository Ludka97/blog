from rest_framework import viewsets, status
from rest_framework.response import Response

from api.games.serializers import GameSerializer
from games.models import Game


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Game.objects.all().order_by("-created_at")
    serializer_class = GameSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Game.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
