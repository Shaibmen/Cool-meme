from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Clients)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class CategoryAdmin(admin.ModelAdmin):
    pass