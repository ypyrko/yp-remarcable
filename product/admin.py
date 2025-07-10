from django.contrib import admin

from product.models import Category, Tag, Product


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
