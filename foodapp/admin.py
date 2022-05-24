from django.contrib import admin
from foodapp.models import FoodImage

# Register your models here.
class FoodImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodImage, FoodImageAdmin)
