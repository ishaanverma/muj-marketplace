from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Product
from favorites.models import Favorite
from .forms import AddProductForm

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		favorite, created = Favorite.objects.get_or_create(user=self.request.user)
		context['favorite'] = favorite
		return context	

class ProductCreateView(CreateView):
	form_class = AddProductForm
	model = Product
	template_name = "products/product_create_form.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class ProductUpdateView(UpdateView):
	form_class = AddProductForm
	model = Product
	template_name = "products/product_update_form.html"

	def get_object(self, *args, **kwargs):
		obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
		if obj.user != self.request.user:
			raise PermissionDenied() #or Http404
		return obj

class ProductDeleteView(DeleteView):
	model = Product
	success_url = reverse_lazy('products:list')

	def get_object(self, *args, **kwargs):
		obj = super(ProductDeleteView, self).get_object(*args, **kwargs)
		if obj.user != self.request.user:
			raise PermissionDenied() #or Http404
		return obj

class UserProductListView(LoginRequiredMixin, ListView):
	login_url = "account:login"
	model = Product
	template_name = "products/list.html"
	paginate_by = 10

	def get_queryset(self):
		return Product.objects.filter(user=self.request.user)
