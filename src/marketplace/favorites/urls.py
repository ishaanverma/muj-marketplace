from django.urls import path

from . import views

app_name = "favorites"

urlpatterns = [
	path('', views.FavoritesView.as_view(), name='home')
]
