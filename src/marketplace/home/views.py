from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from products.models import Product
# class HomeView(View):
# 	template_name = "home/index.html"

class HomeView(TemplateView):
	template_name='home/home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)

		request = self.request
		object_list = Product.objects.featured()
		username = request.user.get_full_name()
		context['object_list'] = object_list
		context['username'] = username
		return context
# def HomeView(request):
# 	context = {}
# 	if request.user.is_authenticated:
# 		context = {
# 			"username": request.user.get_full_name(),
# 		}

# 	return render(request, 'home/home.html', context)
