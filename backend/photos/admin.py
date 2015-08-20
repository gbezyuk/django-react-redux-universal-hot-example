from django.contrib import admin
from .models import Category, Photo
from .models.category.admin import CategoryAdmin
from .models.photo.admin import PhotoAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
