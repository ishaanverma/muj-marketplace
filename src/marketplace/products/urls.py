from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
	path('', views.ProductListView.as_view(), name='list'),
	path('add/', views.ProductCreateView.as_view(), name='add'),
	path('active/', views.UserProductListView.as_view(), name='active'),
	path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='edit'),
	path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='delete'),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
]
