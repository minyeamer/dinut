from django.urls import path
from foodapp.views import temp_upload
from django.conf import settings 

app_name = 'foodapp'

urlpatterns = [
    path('upload/', temp_upload, name='upload'),
]