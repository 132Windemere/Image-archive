# from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import ImageUpload  # , Image
from .serializers import ImageUploadSerializer
from django.views.generic import TemplateView


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageListView(APIView):
    def get(self, request, *args, **kwargs):
        images = ImageUpload.objects.all()
        serializer = ImageUploadSerializer(images, many=True)
        return Response(serializer.data)


class ImageDetailView(generics.RetrieveAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

    # Optional: Custom response handling
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ImageUpload.DoesNotExist:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ImageDeleteView(generics.DestroyAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class HomeView(TemplateView):
    template_name = "home.html"  # Points to the home.html template
