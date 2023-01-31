from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django import forms



class Login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=('Password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))