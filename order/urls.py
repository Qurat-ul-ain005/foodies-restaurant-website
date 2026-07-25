from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_order, name='save_order'),
]