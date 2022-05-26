from django.contrib import admin
from dietapp.models import Nutrition, Diet, DietImage, DailyDietImage

# Register your models here.
class NutritionAdmin(admin.ModelAdmin):
    pass
class DietAdmin(admin.ModelAdmin):
    pass
class DietImageAdmin(admin.ModelAdmin):
    pass
class DailyDietImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(DietImage, DietImageAdmin)
admin.site.register(DailyDietImage, DailyDietImagesAdmin)