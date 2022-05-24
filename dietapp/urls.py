from django.urls import path
from dietapp.views import upload_diet_image

app_name = 'dietapp'

urlpatterns = [
    path('diet/', upload_diet_image, name='upload')
]
