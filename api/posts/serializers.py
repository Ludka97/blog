from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    # author = UserSerializer(read_only=True)
    image = serializers.ImageField(read_only=True)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
