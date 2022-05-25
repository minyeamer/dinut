from django import forms
from dietapp.models import DietImage


class DietImageUploadForm(forms.ModelForm):

    class Meta: 
        model = DietImage 
        fields = ['upload_diet',]
