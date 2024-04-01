from django.urls import path

from .views import PhotoViewSet


urlpatterns = [
    path('photos', PhotoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('photos/<str:pk>', PhotoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
