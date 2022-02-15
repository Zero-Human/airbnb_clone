from dataclasses import fields
from re import search
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class Itemadmin(admin.ModelAdmin):
    """Item Admin"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

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
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "instant_book",
        "city",
        "country",
    )
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    search_fields = ("^city",)  # 검색 기능

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin"""

    pass
