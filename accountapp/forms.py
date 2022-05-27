from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountCreatioinForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class AccountUpdateForm(AccountCreatioinForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
