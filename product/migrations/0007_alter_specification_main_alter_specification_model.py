# Generated by Django 4.0.6 on 2022-08-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основная характеристика/(цветная)'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='spec', to='product.model'),
        ),
    ]
