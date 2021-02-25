from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Meta explains information about form itself
    class Meta:
        model = Item
        fields = ['name', 'done']
