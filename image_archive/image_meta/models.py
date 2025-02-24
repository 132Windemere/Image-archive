from django.db import models
from django.db import models


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default="Untitled")

    def __str__(self):
        return f"Image {self.id}"


class Image(models.Model):
    title = models.CharField(max_length=255)  # Image title
    file = models.ImageField(upload_to="images/")  # Image file

    def __str__(self):
        return self.title
