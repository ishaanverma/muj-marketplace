from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('home/', views.AccountHomeView.as_view(), name='home'),
	path('logout/', auth_views.LogoutView.as_view(next_page="home:home"), name='logout'),
	# path('password_change/'),
	# path('password_change/done/'),
	# path('password_reset/'),
	# path('password_reset/done/'),
]
