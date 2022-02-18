from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from math import ceil


# Create your views here.


def all_rooms(request):
    page = int(request.GET.get("page"))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.get_page(page)
    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms},
    )
