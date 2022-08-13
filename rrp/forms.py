from django import forms
from django.contrib.auth.models import User
from rrp.models import Users


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('picture', )

