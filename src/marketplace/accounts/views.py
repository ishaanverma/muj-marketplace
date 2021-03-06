from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
from django.contrib import messages

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
        else:
            messages.error(request,'Invalid Details, Please Sign Up or Try Again.')
            
        return super(LoginView, self).form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = "/account/login"

class AccountHomeView(LoginRequiredMixin, TemplateView):
    login_url = "account:register"
    template_name = "accounts/home.html"

class UserUpdateView(UpdateView):
    form_class = RegisterForm
    model = User
    template_name = "accounts/user_update_form.html"
    