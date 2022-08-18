from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    release_data = serializers.DateField()
    genre = serializers.CharField(max_length=100)
    platform = serializers.CharField(max_length=20)
    progress = serializers.IntegerField()
    comment = serializers.CharField(max_length=100)
