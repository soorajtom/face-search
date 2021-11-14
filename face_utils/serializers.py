from rest_framework import serializers

class FaceSerializer(serializers.Serializer):
    """
        Serializer for the incoming request.
    """
    image = serializers.ImageField()