import os, datetime, transliterate, cyrtranslit
import uuid
from PIL import Image as PILImage
import json
from urllib.parse import quote

from .forms import *
from .models import *

from django.core.files.storage import FileSystemStorage


def contains_cyrillic(text):
    return any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text)

# сохранение в картинки если картинки, в файлы если docx и тп, сохраняем файл, в записи в таблице сущность к которой прикреплен файл
def save_imeges_to_storage(file):
    try:
        name = str(file)
        print(name)
        if contains_cyrillic(name):
            latinized_name = transliterate.translit(name, reversed=True)
            print(latinized_name)
        else:
            latinized_name = name

        PILImage.open(file)
        fs = FileSystemStorage()
        unique_filename = f"{uuid.uuid4()}_{slugify(latinized_name)}"
        # Сохраните файл на сервере
        filename = fs.save(unique_filename, file)
        # Получите путь к сохраненному файлу
        image_path = fs.url(filename)

        # Создание файла
        image = Image.objects.create(
            image = image_path,
            file_name = latinized_name,
            # message = message_in_file,
        )
        print('Этот Image: ', image)

    except IOError:
        name = str(file)
        print(name)
        if contains_cyrillic(name):
            latinized_name = transliterate.translit(name, reversed=True)
            print(latinized_name)
        else:
            latinized_name = name

        fs = FileSystemStorage() # если не удалось открыть как изображение сохраняяем как обычный файл
        original_filename = file.name
        # file_extension = os.path.splitext(original_filename)[1]
        # unique_filename = f"{uuid.uuid4()}_{slugify(image_file.name)}"
        unique_filename = f"{uuid.uuid4()}_{latinized_name}"
        # encoded_filename = unique_filename.encode('utf-8')
        print(f'unique_filename {unique_filename}')
        # filename = fs.save(unique_filename, image_file)
        filename = fs.save(unique_filename, file)
        filename = quote(filename)
        encoded_text = filename.encode('utf-8')
        fs.save(encoded_text.decode('utf-8'), file)
        # filename += file_extension
        # путь к сохраненному файлу
        image_path = fs.url(encoded_text.decode('utf-8'))
        add_task_file = Image.objects.create(
            file = image_path,
            file_name = latinized_name,
        )
        print('Это документ: ', add_task_file)