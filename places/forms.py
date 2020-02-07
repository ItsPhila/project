from django import forms
from .models import Places

class AddPlace(forms.ModelForm):
    class Meta:
        model = Places
        exclude = ['author','pubdate']
        fields= ['title','myimage','location']