from django.contrib import admin
from .models import Page
from .models.page.admin import PageAdmin

admin.site.register(Page, PageAdmin)
