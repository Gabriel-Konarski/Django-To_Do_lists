from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name="lists"),
    path("create/", views.addList, name="create"),
    path("delete-list/<str:pk>/", views.deleteList, name="delete-list"),
    path("delete-item/<str:pk>/", views.deleteItem, name="delete-item"),
    path("view/<str:pk>/", views.viewList, name="view"),
]