from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStampedModel):
    """List"""

    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists")

    def __str__(self):
        return f"{self.name}"

    def count_rooms(slef):
        return slef.rooms.count()

    count_rooms.short_description = "Number of Rooms"
