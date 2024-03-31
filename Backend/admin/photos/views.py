from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.
class PhotoViewSet(viewsets.ViewSet):
    def list(self, request):
        photos = Photo.objects.all()
        serializer =  PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        photo = get_object_or_404(Photo, id=pk)
        serializer =  PhotoSerializer(photo)
        return Response(serializer.data)


    def update(self, request, pk=None):
        photo = get_object_or_404(Photo, id=pk)
        serializer = PhotoSerializer(data=request.data, instance=photo)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        photo = get_object_or_404(Photo, id=pk)
        photo.delete()
        return Response({'detail':'photo has been deleted.'}, status=status.HTTP_204_NO_CONTENT)
