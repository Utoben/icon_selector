from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, JsonResponse, HttpResponseNotFound

from django.contrib.auth.decorators import permission_required, login_required

from .tasks import *
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

def bucket(request):
    error = ''
    title = 'Ваши значки'

    icons = Image.objects.filter(is_choised=True)
    count = Image.objects.filter(is_choised=True).count

    context = {
        'title': title,
        'error': error,
        'icons': icons,
        'count': count,
    }
    return render(request, 'main/bucket.html', context)

def choise(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)
        image.is_choised = True
        image.save()

        print(f'Картинка {image.pk} выбрана: {image.is_choised}')
        return JsonResponse({'success': True,})
    else:
        return JsonResponse({'success': False})
    

def clear_bucket(request):
    if request.method == 'POST':
        icons = Image.objects.filter(is_choised=True)
        for icon in icons:
            icon.is_choised = False
            icon.save()
        print(f'Корзина очищена')
        return JsonResponse({'success': True,})
    else:
        return JsonResponse({'success': False})

def send_order(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        print(f'Пришли: {fullname} {phone} {email}')

        long_send_order_email(fullname, phone, email)
        
        return JsonResponse({'success': True,})
    else:
        return JsonResponse({'success': False})
        
  
