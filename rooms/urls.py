from django.urls import path
from rooms import views as room_view

app_name = "rooms"
# function
# urlpatterns = [path("<int:pk>", room_view.room_detail, name="detail")]
# class
urlpatterns = [
    path("<int:pk>", room_view.RoomDetail.as_view(), name="detail"),
    path("search", room_view.search, name="search"),
]
