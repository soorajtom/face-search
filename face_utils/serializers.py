from rest_framework import serializers

class FaceSerializer(serializers.Serializer):
    image = serializers.ImageField()