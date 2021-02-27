from django import forms
from .models import Data


class ItemForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['food_name', 'food_desc', 'food_price', 'food_image']