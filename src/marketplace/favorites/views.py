from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite

def FavoritesView(request):
    queryset = Favorite.objects.all()
    context = {
        "objects": queryset,
    }
    return render(request, 'favorites/favorites_list.html', context)
