from django import forms
from django.contrib.auth import get_user_model

class PostProductForm(forms.Form):
    image = forms.ImageField(label='Product Image')
    title = forms.CharField(widget=forms.TextInput(attrs={
                                "class": "post-ad-form",
                                "placeholder": "Product Title",
                                }
                            ), label='Title')
    price = forms.DecimalField(max_digits=10, decimal_places=2,
                                widget=forms.NumberInput(attrs={
                                    "class": "post-ad-form",
                                    "placeholder": "Product Price",
                                }
                            ), label='Price')
    description = forms.CharField(widget=forms.Textarea(attrs={
                                    "class": "post-ad-form",
                                    "placeholder": "Product description"
                                    }
                                ), label='Product Description')
