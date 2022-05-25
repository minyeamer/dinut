from django.contrib import admin
from foodapp.models import FoodImage, Nutrition

# Register your models here.
class FoodImageAdmin(admin.ModelAdmin):
    pass
class NutritionAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodImage, FoodImageAdmin)
admin.site.register(Nutrition, NutritionAdmin)
