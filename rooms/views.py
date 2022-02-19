from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import DetailView
from django_countries import countries
from django.core.paginator import Paginator
from . import models


# Create your views here.


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.get_page(page)
    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms},
    )


# function
"""def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", {"room": room})

    except models.Room.DoesNotExist:
        raise Http404()"""
# class
class RoomDetail(DetailView):

    model = models.Room


def search(request):
    city = str.capitalize(request.GET.get("city", "Anywhere"))
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
