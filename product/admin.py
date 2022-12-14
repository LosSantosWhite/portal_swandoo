from django.contrib import admin

from product.models import Category, Model, Description, Specification, Variety, Gallery, Color, RewardsImage, Slider, \
    Feature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ['model', 'barcode', 'color', 'price']


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['model', 'title', 'text']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(RewardsImage)
class RewardsImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'model']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['variety', 'image']


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url_to']
    list_editable = ['title', 'url_to']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'image']
