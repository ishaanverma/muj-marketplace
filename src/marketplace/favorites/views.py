from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite

# def FavoritesView(request):
#     queryset = Favorite.objects.all()
#     context = {
#         "objects": queryset,
#     }
#     return render(request, 'favorites/favorites_list.html', context)

class FavoritesView(ListView):
    model = Favorite
    template_name = 'favorites/favorites_list.html'

    # def favorite(self, pk):
    #     request = self.request
    #     user = request.user
    #     Favorite.user = user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
