from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('category', 'title', 'description', 'image','price', 'condition', 'top_size', 'bottom_size', 'shoe_size',)