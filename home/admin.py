from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class ModelCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

@admin.register(models.Images)
class ModelImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'img', 'cat_foreign']