from django.contrib import admin
from profileapp.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    radio_fields = {'gender':admin.VERTICAL, 'activity':admin.VERTICAL}

admin.site.register(Profile, ProfileAdmin)
