from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
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
