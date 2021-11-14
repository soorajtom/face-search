from rest_framework import serializers

class FaceSerializer(serializers.Serializer):
    """
        Serializer for the incoming face request.
    """
    image = serializers.ImageField()

class ImagePathSerializer(serializers.Serializer):
    """
        Serializer for an authenticated message request.
    """
    path = serializers.CharField()

class ImageBase64Serializer(serializers.Serializer):
    """
        Serializer for an authenticated message request.
    """
    path = serializers.CharField()
    base64 = serializers.CharField()