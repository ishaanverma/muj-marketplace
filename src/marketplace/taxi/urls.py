from django.urls import path

from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.TaxiListView.as_view(), name='home'),
	path('add/', views.TaxiCreateView.as_view(), name='add'),
	# path('active/', views.UserProductListView.as_view(), name='active'),
	# path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='edit'),
	# path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='delete'),
	path('<slug:slug>/', views.TaxiDetailView.as_view(), name='detail'),
	
]
