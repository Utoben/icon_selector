from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, JsonResponse, HttpResponseNotFound

from django.contrib.auth.decorators import permission_required, login_required

from django.core.mail import send_mail

from .forms import *
from .models import *
from .utils import *


def custom_404(request):
    return render(request, 'main/404.html', status=404)

def home(request):
    title = 'Выберите изображения'
    images = Image.objects.all()

    context = {
        'title': title,
        'images': images,
    }

    return render(request, 'main/home.html', context)

def add_images(request):

    if request.method == "POST":
        print(request)
        image_files = request.FILES.getlist('image_list')
        print(image_files)
        for image in image_files:
            # PILImage.open(image)
            # fs = FileSystemStorage()
            # filename = fs.save(image, filename)
            # image_path = fs.url(image, filename)
            # add_file = Image.objects.create(
            #     file = image_path,
            #     file_name = image_path,
            # )
            # add_file.save()
            save_imeges_to_storage(image)
            print(image)
        return JsonResponse({'message': 'Сохранено'})
    else:
        return JsonResponse({'error': 'Файл не был передан'}, status=400)
        
def add_images_page(request):
    error = ''
    title = 'Выберите изображения'
    context = {
        'title': title,
        'error': error,
    }

    return render(request, 'main/add.html', context)

def choise(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)
        image.is_choised = True
        image.save()
        return JsonResponse({'image': image.is_choised}, {'success': True,})
    else:
        return JsonResponse({'success': False})