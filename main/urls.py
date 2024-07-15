from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    # страницы
    path('', views.home, name='home'),
    path('add_images_page/', views.add_images_page, name='add_images_page'),
    path('bucket/', views.bucket, name='bucket'),

    # роуты
    path('add_images/', views.add_images, name='add_images'),
    path('choise/', views.choise, name='choise'),
    path('clear_bucket/', views.clear_bucket, name='clear_bucket'),
    path('send_order/', views.send_order, name='send_order'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
