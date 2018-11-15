from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = "/account/login"

class SettingsView(TemplateView):
    template_name = "accounts/settings.html"

class UserUpdateView(UpdateView):
    form_class = RegisterForm
    model = User
    template_name = "accounts/user_update_form.html"
    