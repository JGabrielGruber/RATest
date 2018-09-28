from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):

    list_display        = ["__unicode__", "updated", "timestamp"]
    list_display_links  = ["updated"]
    list_filter         = ["timestamp"]
    search_fields       = ["__unicode__"]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
