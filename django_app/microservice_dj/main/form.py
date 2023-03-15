from django import forms

from .models import User


class AuthForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='input password')
    class Meta:
        fields = "__all__"
        model = User
