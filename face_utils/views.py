import os
import base64

from django.conf import settings
from django.views.generic import base
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, permissions, status
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from face_utils.serializers import (FaceSerializer, ImageBase64Serializer,
                                    ImagePathSerializer)


class ListSimilarFaces(APIView):
    """
    View to list all similar faces against the request sent.

    * Requires token authentication.
    """
    parser_classes = (FormParser, MultiPartParser, FileUploadParser)
    renderer_classes = (JSONRenderer,)
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = FaceSerializer

    @swagger_auto_schema(
        operation_id= 'face_search',
        request_body = FaceSerializer, 
        manual_parameters=[openapi.Parameter(
                            name="image",
                            in_=openapi.IN_FORM,
                            type=openapi.TYPE_FILE,
                            required=True,
                            description="Face Image"
                            )],
        responses={400: 'Invalid data in uploaded file',
                   200: 'Success'},
    )
    def post(self, request, format=None):
        """
        Return a list of all similar faces.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data

        return Response("Success!")


class RetrieveImage(APIView):
    """
    Return the base64 string for the requested image path.

    * Requires token authentication.
    """
    renderer_classes = (JSONRenderer,)
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ImagePathSerializer

    @swagger_auto_schema(
        operation_id= 'face_search',
        request_body = ImagePathSerializer, 
        responses={400: 'Invalid data',
                   404: 'Requested Image path not found',
                   200: ImageBase64Serializer},
    )
    def post(self, request, format=None):
        """
        Return the base64 string for the requested image path.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data

            if not self.validate_image_path(data):
                return Response('Requested Image path not found', status=status.HTTP_404_NOT_FOUND)

            base64_data = self.get_base64_string(data)

            # use the response serialiser to complete the request
            serialised_response = ImageBase64Serializer(
                data={'path': data["path"], 'base64': base64_data})

            if serialised_response.is_valid(raise_exception=True):
                return Response(serialised_response.data)

    def validate_image_path(self, path_data):
        '''
            Validate if the image path exists in the base image directory.
        '''
        full_path = os.path.join(settings.IMAGES_DIR, path_data["path"])
        
        return os.path.exists(full_path)

    def get_base64_string(self, path_data):
        '''
            Convert the image to base64 string.
        '''
        full_path = os.path.join(settings.IMAGES_DIR, path_data["path"])
        
        data = ''
        with open(full_path, "rb") as image_file:
            data = base64.b64encode(image_file.read()).decode('utf-8')
            
        return data
