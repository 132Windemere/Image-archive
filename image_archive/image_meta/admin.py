from django.contrib import admin
from .models import ImageUpload
from django.contrib import admin
from django.utils.html import format_html
from .models import ImageUpload

@admin.register(ImageUpload)
class ImageUploadCreateAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_thumbnail', 'image_name', 'file_size', 'uploaded_at')  # Adding the new fields

    # Method to show the image name
    def image_name(self, obj):
        return obj.image.name.split('/')[-1]  # Extracts the file name from the path

    # Method to show the file size
    def file_size(self, obj):
        return f"{obj.image.size / 1024:.2f} KB"  # Converts size to KB for readability

    # Method to show image thumbnail
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "No image"
    
    # Optional: You can set descriptive names for the columns
    image_name.short_description = 'Image Name'
    file_size.short_description = 'File Size (KB)'
