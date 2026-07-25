from django.urls import path
from . import views

urlpatterns = [
    path("save/", views.save_contact, name="save_contact"),
]