from django.shortcuts import render
from django.views import View

# class HomeView(View):
# 	template_name = "home/index.html"

def HomeView(request):
	context = {}
	if request.user.is_authenticated:
		context = {
			"username": request.user.get_full_name(),
		}

	return render(request, 'home/home.html', context)
