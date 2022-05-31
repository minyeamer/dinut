from django.urls import path
from dietapp.views import DietUploadView, DailyDietView, home

app_name = 'dietapp'

urlpatterns = [
    path('upload/', DietUploadView.as_view(), name='upload'),
    path('daily/', DailyDietView.index, name='daily'),
    path('daily/detail/', DailyDietView.detail, name='detail'),
    path('daily/update/', DailyDietView.update, name='update'),
    path('daily/delete/', DailyDietView.delete, name='delete'),
]