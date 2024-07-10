# Generated by Django 4.2.5 on 2024-07-10 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('file', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Документ')),
                ('file_name', models.TextField(blank=True, null=True, verbose_name='Имя файла')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки: ')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]