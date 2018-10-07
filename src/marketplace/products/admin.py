from django.contrib import admin

# Register your models here.
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug', 'category']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug']
	prepopulated_fields = {"slug": ("name",)}
	class Meta:
		model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
