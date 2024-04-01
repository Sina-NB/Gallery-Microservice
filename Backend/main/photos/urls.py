from django.urls import path

from .views import ListPhotos, LikePhoto


urlpatterns = [
    path('photos', ListPhotos.as_view()),
    path('photos/<int:pk>/like', LikePhoto.as_view())
]
