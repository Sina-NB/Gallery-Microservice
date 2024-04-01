from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer
from .producer import Publisher

# Create your views here.
class ListPhotos(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

class LikePhoto(APIView):

    def post(self, request, pk):
        photo = get_object_or_404(Photo, id=pk)
        photo.likes += 1
        photo.save()
        serializer = PhotoSerializer(photo)
        publisher = Publisher()
        publisher.publish('update', serializer.data)
        publisher.close()
        return Response(serializer.data)
