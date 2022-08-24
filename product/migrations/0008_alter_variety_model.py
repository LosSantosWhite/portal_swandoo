# Generated by Django 4.0.6 on 2022-08-24 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_specification_main_alter_specification_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variety', to='product.model'),
        ),
    ]