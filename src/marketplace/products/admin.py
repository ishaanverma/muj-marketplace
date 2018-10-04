from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)