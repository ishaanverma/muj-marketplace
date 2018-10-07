from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    # A form for creating new users.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # check the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.confirm = True
            user.save()

        return user

class UserAdminChangeForm(forms.ModelForm):
    # A form for updating users.
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',
                    'admin', 'staff', 'confirm', 'active')

    def clean_password(self):
        return self.initial["password"]

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                "class": "form-control",
                                "placeholder": "Enter Email",
                                }
                            ), label='Email')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                "class": "form-control",
                                "placeholder": "Enter Password",
                                }
                            ), label='Password')



class RegisterForm(forms.ModelForm):
    # A form for creating new users.
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={
                                    "class": "form-control",
                                    "placeholder": "Enter Password",
                                }))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={
                                    "class": "form-control",
                                    "placeholder": "Enter Password Again"
                                }))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        widgets = {
            "email": forms.EmailInput(attrs={
                        "class": "form-control",
                        "placeholder": "Enter Email",
                    }),
            "first_name": forms.TextInput(attrs={
                        "class": "form-control",
                        "placeholder": "Enter First Name",
                    }),
            "last_name": forms.TextInput(attrs={
                        "class": "form-control",
                        "placeholder": "Enter Last Name",
                    }),
        }

    def clean_password2(self):
        # check the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
