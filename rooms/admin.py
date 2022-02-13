from dataclasses import fields
from re import search
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class Itemadmin(admin.ModelAdmin):
    """Item Admin"""

    pass


@admin.register(models.Room)
class RoomsAdmin(admin.ModelAdmin):
    """Room Admin"""

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
    )
    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    search_fields = ("^city",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin"""

    pass
