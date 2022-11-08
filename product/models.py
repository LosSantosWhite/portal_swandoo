from email.policy import default
import os
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.core.validators import FileExtensionValidator


def upload_photo_variety(instance, filename):
    return os.path.join(
        "static", "products", instance.model.name, instance.barcode, filename
    )


def upload_photo_rewards(instance, filename):
    return os.path.join(
        "static",
        "products",
        instance.model.name,
        "rewards",
        instance.name + os.path.splitext(filename)[-1],
    )


def upload_photo_color(instance, filename):
    return os.path.join(
        "static", "products", "colors", instance.name + os.path.splitext(filename)[-1]
    )


def upload_photo_gallery(instance, filename):
    return os.path.join(
        "static", "products", instance.variety.model.name, "photos", filename
    )


def upload_icons(instance, filename):
    return os.path.join("static", "products", instance.model.name, "icons", filename)


def upload_descr_photo(instance, filename):
    return os.path.join("static", "products", "features", filename)


def upload_slider_image(instance, file_name):
    return os.path.join("static", "products", "slider", file_name)


class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)

    def __str__(self):
        return self.name


class Feature(models.Model):
    title = models.CharField("Заголовок колонки", max_length=30, blank=True, null=True)
    text = models.CharField("Описание колонки", max_length=150, blank=True, null=True)
    image = models.ImageField(
        verbose_name="Картинка колонки",
        blank=True,
        null=True,
        upload_to=upload_descr_photo,
    )


class Description(models.Model):
    name = models.CharField("Название описания", max_length=50)
    h1 = models.CharField("Заголовок h1", max_length=50, blank=True, null=True)
    h2 = models.CharField("Подзаголовок h2", max_length=50, blank=True, null=True)
    reward_title = RichTextField(
        verbose_name="Заголовок секции с наградами", blank=True, null=True
    )

    heading_2_header = RichTextField(
        verbose_name="Текст секции №2", blank=True, null=True
    )
    features = models.ManyToManyField(
        Feature,
        help_text="Желательно не больше 3 на 1 модель",
        verbose_name="Спец. возмодности",
    )
    color_section_title = models.CharField(
        "Заголовок секции с цветами", max_length=30, blank=True, null=True
    )
    color_section_subtitle = models.CharField(
        "Подзаголовок секции цветов",
        default="Какой Ваш любимый?",
        max_length=30,
        blank=True,
        null=True,
    )
    video_section_title = models.CharField(
        "Заголовок для секции видео",
        default="Как использовать",
        max_length=30,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class VideoUrl(models.Model):
    heading_4_video_1 = models.URLField("Ссылка на видео", blank=True, null=True)
    descr = models.ForeignKey(
        Description, on_delete=models.PROTECT, related_name="video_urls"
    )

    def __str__(self):
        return f"Video #{self.id} for {self.descr.model.name}"


class Color(models.Model):
    name = models.CharField("Название цвета", max_length=20, unique=True)
    image = models.FileField(
        "Иконка цвета",
        upload_to=upload_photo_color,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["svg", "jpeg", "jpg", "png"])],
    )

    def __str__(self):
        return self.name


class Model(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField("Название модели", max_length=50)
    description = models.OneToOneField(Description, on_delete=models.PROTECT)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.slug])


class RewardsImage(models.Model):
    name = models.CharField("Название награды", max_length=20)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=upload_photo_rewards, blank=True, null=True)
    small = models.BooleanField("Уменьшенный размер иконки", default=False)

    def __str__(self):
        return f"{self.model.name} -- {self.name}"


class Specification(models.Model):
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name="spec")
    title = models.CharField("Заголовок", max_length=30)
    text = models.CharField("Описание", max_length=30)
    image = models.ImageField("Картинка", upload_to=upload_icons, null=True, blank=True)
    main = models.BooleanField("Основная характеристика/(цветная)", default=False)

    def __str__(self):
        return f"{self.model.name} -- {self.title}"


class Variety(models.Model):
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name="variety")
    barcode = models.CharField("Артикул товара", max_length=12, unique=True)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    main_photo = models.ImageField("Главная фотография", upload_to=upload_photo_variety)

    def __str__(self):
        return f"{self.model.name} - {self.color.name} - {self.barcode}"


class Gallery(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=upload_photo_gallery)


class Slider(models.Model):
    title = models.CharField(
        "Заголовок слайдера", max_length=100, default="Заголовок слайдера"
    )
    description = models.CharField(
        "Краткое описание слайдера", max_length=100, default=""
    )
    image = models.ImageField(
        "Картинка слайдера", upload_to=upload_slider_image, default=""
    )
    button_text = models.CharField(
        "Текст кнопки", max_length=30, default="Текст кнопки"
    )
    url_to = models.URLField("Ссылка на страницу", default="/")
    active = models.BooleanField("Активный слайд", default=False)
