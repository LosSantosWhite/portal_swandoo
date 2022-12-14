# Generated by Django 4.0.6 on 2022-08-10 15:16

import django.core.validators
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_specification_image_delete_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=product.models.upload_photo_color, validators=[django.core.validators.FileExtensionValidator(['svg', 'jpeg', 'jpg', 'png'])], verbose_name='Иконка цвета'),
        ),
    ]
