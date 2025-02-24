from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ImageUploadView,
    ImageListView,
    ImageDetailView,
    ImageDeleteView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("upload/", ImageUploadView.as_view(), name="image-upload"),
    path("images/", ImageListView.as_view(), name="image-list"),
    path("images/<int:pk>/", ImageDetailView.as_view(), name="image-detail"),
    path("images/<int:pk>/delete/", ImageDeleteView.as_view(), name="image-delete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
