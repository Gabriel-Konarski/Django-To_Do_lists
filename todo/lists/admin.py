from django.contrib import admin

from .models import Category, List, Item

# Register your models here.
admin.site.register(Category)
admin.site.register(List)
admin.site.register(Item)