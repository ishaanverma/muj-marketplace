from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('settings/', views.SettingsView.as_view(), name='settings'),
	# path('logout/'),
	# path('password_change/'),
	# path('password_change/done/'),
	# path('password_reset/'),
	# path('password_reset/done/'),
]
