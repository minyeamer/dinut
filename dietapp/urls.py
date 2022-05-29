from django.urls import path
from dietapp.views import DietUploadView, DailyDietView, home

app_name = 'dietapp'

urlpatterns = [
    path('upload/', DietUploadView.as_view(), name='upload'),
    path('daily/', DailyDietView.as_view(), name='daily'),
    path('home/',  home, name='home')
]
