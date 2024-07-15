from django.contrib import admin
from .models import *

class Image_Admin(admin.ModelAdmin):
    list_display = ["file_name", "file", "image", "created_at", ] 
class UserProfile_Admin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]

admin.site.register(Image, Image_Admin)
admin.site.register(UserProfile, UserProfile_Admin)