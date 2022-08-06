from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ["id","name","category","price","is_active"]
    list_filter = ["is_active","price"]
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
