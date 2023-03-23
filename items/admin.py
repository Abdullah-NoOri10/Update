from django.contrib import admin
from .models import Companie, Product,Category

# Register your models here.

admin.site.register(Companie)
admin.site.register(Product)
admin.site.register(Category)
