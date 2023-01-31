from django import forms
from .models import Homepost




class Homeadd(forms.ModelForm):
    class Meta:
        model=Homepost
        fields=['title','text']
        labels={'title':'Title',"text":'Comment'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.TextInput(attrs={'class':'form-control'}),
            }