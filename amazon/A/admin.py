from django.contrib import admin
from .models import Product,Category
class ProductAdmin(admin.ModelAdmin):
    list=('name','price','stock','image')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
# Register your models here.
