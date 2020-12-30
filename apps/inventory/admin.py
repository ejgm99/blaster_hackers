from django.contrib import admin

# Register your models here.
from .models import Item,Type

admin.site.register(Item)
admin.site.register(Type)
