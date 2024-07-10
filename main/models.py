from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User
# from . import views
# from  views import edit_task_view
from django.utils.text import slugify
from django.utils import timezone



class Image(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images', null=True, verbose_name='Задача',)
    image = models.ImageField('Изображение', null=True, upload_to='images/', blank=True)
    file = models.FileField('Документ',null=True ,upload_to='images/', blank=True)
    file_name = models.TextField('Имя файла', null=True, blank=True,)
    created_at = models.DateTimeField(default=timezone.now,  verbose_name='Дата загрузки: ',)

    is_choised = models.BooleanField('Выбрано', null=True, blank=True , default=False)
    
    def __str__(self):
        return self.file_name

    # def save(self, *args, **kwargs):
    #     self.file_name = slugify(self.file.name)
    #     super(Image, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
