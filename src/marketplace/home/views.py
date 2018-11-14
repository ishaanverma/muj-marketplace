from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from products.models import Product

class HomeView(TemplateView):
	template_name='home/home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)

		request = self.request
		featured = Product.objects.featured()[:4]
		electronics =  Product.objects.filter(category__slug='electronics')[:4]
		books = Product.objects.filter(category__slug='books')[:4]
		accessories = Product.objects.filter(category__slug='accessories')[:4]

		context['featured'] = featured
		context['electronics'] = electronics
		context['books'] = books
		context['accessories'] = accessories
		
		return context