# Generated by Django 4.0.6 on 2022-08-03 15:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название цвета')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.upload_photo_color, verbose_name='Иконка текста')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название описания')),
                ('h1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок h1')),
                ('h2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Подзаголовок h2')),
                ('heading_1_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Заголовок секции с наградами')),
                ('heading_2_header', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст секции №2')),
                ('heading_2_image_1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка колонки 1')),
                ('heading_2_image_1_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок колонки 1')),
                ('heading_2_image_1_text', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание колонки 1')),
                ('heading_2_image_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка колонки 2')),
                ('heading_2_image_2_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок колонки 2')),
                ('heading_2_image_2_text', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание колонки 2')),
                ('heading_2_image_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка колонки 3')),
                ('heading_2_image_3_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок колонки 3')),
                ('heading_2_image_3_text', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание колонки 3')),
                ('heading_3_title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок секции с цветами')),
                ('heading_3_subtitle', models.CharField(blank=True, default='Какой Ваш любимый?', max_length=30, null=True, verbose_name='Подзаголовок секции цветов')),
                ('heading_4_title', models.CharField(blank=True, default='Как использовать', max_length=30, null=True, verbose_name='Заголовок для секции видео')),
                ('heading_4_video_1', models.URLField(blank=True, null=True, verbose_name='Видео №1')),
                ('heading_4_video_2', models.URLField(blank=True, null=True, verbose_name='Видео №2')),
                ('heading_4_video_3', models.URLField(blank=True, null=True, verbose_name='Видео №3')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название модели')),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
                ('description', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='product.description')),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=12, unique=True, verbose_name='Артикул товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('main_photo', models.ImageField(upload_to=product.models.upload_photo_variety, verbose_name='Главная фотография')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.color')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.model')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=30, verbose_name='Описание')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.model')),
            ],
        ),
        migrations.CreateModel(
            name='RewardsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название награды')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.upload_photo_rewards)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.model')),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название иконки')),
                ('image', models.ImageField(upload_to=product.models.upload_icons, verbose_name='Картинка')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.specification')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=product.models.upload_photo_gallery)),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.variety')),
            ],
        ),
    ]
