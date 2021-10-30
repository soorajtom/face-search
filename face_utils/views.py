from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from face_utils import serializers
from drf_yasg.utils import swagger_auto_schema

from face_utils.serializers import FaceSerializer


class ListSimilarFaces(APIView):
    
    """
    View to list all similar faces against the request sent.

    * Requires token authentication.
    """
    authentication_classes = [authentication.TokenAuthentication]

    @swagger_auto_schema(request_body=FaceSerializer,responses={200: FaceSerializer,400: 'Bad Request'})
    def post(self, request, format=None):
        """
        Return a list of all similar faces.
        """
        serializer = FaceSerializer(request.data)
        
        return Response()

