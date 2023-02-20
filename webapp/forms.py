from django import forms
from .models import Product
from .models import Category

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'image', 'category', 'description')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
        }

