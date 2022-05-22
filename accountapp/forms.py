from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class AccountCreatioinForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email','password1','password2','username','height',
                    'weight','age','gender','activity')

    def calc_bmr(self, gender: str, weight: int, height: int, age: int) -> int:
        # Mifflin-St. Jeor Caculator
        if gender == 'M':
            return int(10*weight + 6.25*height - 5*age + 5)
        else:
            return int(10*weight + 6.25*height - 5*age - 161)

    def calc_caloric_burn(self, bmr: int, activity: str) -> int:
        # Mifflin-St. Jeor Caculator

        activity_level = {
            'sedentary':1.2,
            'slightly':1.375,
            'moderately':1.55,
            'very':1.725,
            'extra':1.9,
        }

        return int(bmr * activity_level[activity])

    def save(self, commit=True):
        user = super(AccountCreatioinForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.bmr = self.calc_bmr(user.gender, user.weight, user.height, user.age)
        user.caloric_burn = self.calc_caloric_burn(user.bmr, user.activity)
        if commit:
            user.save()
        return user


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
