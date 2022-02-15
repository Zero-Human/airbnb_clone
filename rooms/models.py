from abc import abstractmethod
from distutils.command.upload import upload
from tabnanny import check
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):
    """AbstractItem"""

    name = models.CharField(max_length=140, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):

    """Amenity"""

    class Meta:
        verbose_name_plural = "Amenities"


class RoomType(AbstractItem):
    """RoomType"""

    class Meta:
        verbose_name = "Room Type"


class Facility(AbstractItem):
    """Facility"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """Photo"""

    caption = models.CharField(max_length=140)
    file = models.ImageField(upload_to="rooms")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    discroption = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms")
    facilities = models.ManyToManyField("Facility", related_name="rooms")
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms")

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)
