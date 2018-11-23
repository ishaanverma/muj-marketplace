from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth, messages


from .models import Favorite
from products.models import Product

class FavoritesView(LoginRequiredMixin, ListView):
    login_url = "account:login"
    model = Favorite
    template_name = 'favorites/favorites_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class UpdateFavoriteView(LoginRequiredMixin, View):
    model = None

    def post(self, request):
        product_id = request.POST.get('product_id')
        if product_id is not None:
            try:
                product_obj = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                messages.error(request, 'Product Does Not Exist')

            favorite, created = Favorite.objects.get_or_create(user=request.user)

            if product_obj in favorite.products.all():
                favorite.products.remove(product_obj)
            else:
                favorite.products.add(product_obj)
                
        return redirect("favorites:home")
