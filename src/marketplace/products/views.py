from django.views.generic import ListView, DetailView, FormView
from .forms import PostProductForm
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

class PostProductView(FormView):
	form_class = PostProductForm
	template_name = "products/postad.html"
	success_url = "/products/"

	def form_valid():
		request = self.request
		image = form.cleaned_data['image']
		title = form.cleaned_date['title']
		price = form.cleaned_data['price']
		description = form.cleaned_data['description']
		print(title)
		return redirect("/products/")
