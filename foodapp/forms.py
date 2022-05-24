from django import forms
from foodapp.models import FoodImage


class FoodImageUploadForm(forms.ModelForm):

    class Meta: 
        model = FoodImage 
        fields = ['food_image',]
