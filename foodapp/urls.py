from django.urls import path
from foodapp.views import upload_food_image

app_name = 'foodapp'

urlpatterns = [
    path('upload/', upload_food_image, name='upload'),
]
