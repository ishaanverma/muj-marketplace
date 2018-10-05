from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Product

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

class ProductCreateView(CreateView):
	model = Product
	fields = ['title', 'description', 'price', 'image']
	template_name = "products/product_create_form.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class ProductUpdateView(UpdateView):
	model = Product
	fields = ['title', 'description', 'price', 'image']
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
