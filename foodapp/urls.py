from django.urls import path
from foodapp.views import temp_upload
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'foodapp'

urlpatterns = [
    path('upload/', temp_upload, name='upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 