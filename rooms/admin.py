from django.contrib import admin
from django.utils.html import mark_safe  # 장고에게 안전한 것이라고 지정
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class Itemadmin(admin.ModelAdmin):
    """Item Admin"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):
    # 중간에 해당 기능을 넣어줄 수 있다.
    model = models.Photo


@admin.register(models.Room)
class RoomsAdmin(admin.ModelAdmin):
    """Room Admin"""

    inlines = (PhotoInline,)
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

    raw_id_fields = ("host",)  #  작은 admin 같은 느낌으로 만듬

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

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src ="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
