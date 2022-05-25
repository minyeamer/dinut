from django.urls import path
from dietapp.views import diet_upload_view, daily_diet_view

app_name = 'dietapp'

urlpatterns = [
    path('upload/', diet_upload_view, name='upload'),
    path('daily/', daily_diet_view, name='daily'),
]
