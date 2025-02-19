from django.urls import path
from .views import ImageUploadView, ImageListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('images/', ImageListView.as_view(), name='image-list'),
]
