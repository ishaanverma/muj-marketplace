from django.contrib import admin

# Register your models here.
from .models import Taxi

class TaxiAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Taxi

admin.site.register(Taxi, TaxiAdmin)