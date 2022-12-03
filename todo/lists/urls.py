from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name="lists"),
    path("create/", views.addList, name="create"),
    path("delete/<str:pk>/", views.deleteList, name="delete"),
    path("view/<str:pk>/", views.viewList, name="view"),
]