from django.contrib import admin
from .models import *

class Image_Admin(admin.ModelAdmin):
    list_display = ["file_name", "file", "image", "created_at", ] 


admin.site.register(Image, Image_Admin)