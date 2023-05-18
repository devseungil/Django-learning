from django import forms
from .models import Article

class Articleform(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Article