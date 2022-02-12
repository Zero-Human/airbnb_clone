from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class Itemadmin(admin.ModelAdmin):
    """custom Item Admin"""

    pass


@admin.register(models.Room)
class Roomsadmin(admin.ModelAdmin):
    """custom Room Admin"""

    pass
