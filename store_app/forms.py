from django import forms
from .models import *

class PicForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'pic']