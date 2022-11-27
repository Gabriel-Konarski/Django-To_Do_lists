from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name="lists"),
    path("/create", views.lists, name="create"),
    path("/view", views.lists, name="view"),
]