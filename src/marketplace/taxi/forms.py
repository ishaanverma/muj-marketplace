from django import forms
from .models import Taxi

class AddTaxiForm(forms.ModelForm):
    class Meta:
        model = Taxi
        fields = ['title', 'description', 'leave_date']
        widgets = {
            "title": forms.TextInput(attrs={
                            "class": "form-control",
                            "placeholer": "Enter Name",
                        }),
            "description": forms.Textarea(attrs={
                            "class": "form-control",
                            "placeholer": "Please mention time and number of people you want.",
                        }),
            "leave_date": forms.SelectDateWidget(attrs={
                            "class": "form-control"
            }),
        }