from django import forms
from profileapp.models import Profile
from .models import GENDERS, ACTIVITY


class ProfileCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(label='성별', choices=GENDERS, widget=forms.RadioSelect)
    activity = forms.ChoiceField(label='활동 및 운동 수준', choices=ACTIVITY, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ['nickname','height','weight','age','gender','activity']
