from django.urls import path
from . import views

urlpatterns = [
    path("save/", views.save_reservation, name="save_reservation"),
]