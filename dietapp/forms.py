from django import forms
from dietapp.models import DietImage, DailyDietImage


class DietImageUploadForm(forms.ModelForm):

    class Meta: 
        model = DietImage 
        fields = ['upload_diet',]

class DailyImageUploadForm(forms.ModelForm):
    class Meta: 
        model = DailyDietImage 
        fields = ['morning_diet','lunch_diet','dinner_diet','snack_diet']
