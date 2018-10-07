from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']
        widgets = {
    		"title": forms.TextInput(attrs={
                            "class": "form-control",
                            "placeholer": "Enter Name",
                        }),
    		"description": forms.Textarea(attrs={
                            "class": "form-control",
                            "placeholer": "Enter Description",
                        }),
    		"price": forms.NumberInput(attrs={
                            "class": "form-control",
                            "placeholer": "Enter Price",
                        }),
    		"image": forms.FileInput(attrs={
                            "class": "form-control-file",
    						"type": "file",
                        }),
    	}
