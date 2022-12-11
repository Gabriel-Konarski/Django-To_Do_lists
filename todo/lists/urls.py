from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name="lists"),
    path("create/", views.addList, name="create"),
    path("account/", views.userDetail, name="account"),
    path("view/<str:pk>/", views.viewList, name="view"),
    path("delete-list/<str:pk>/", views.deleteList, name="delete-list"),
    path("delete-item/<str:pk>/", views.deleteItem, name="delete-item"),
    path("delete-category/<str:pk>/", views.deleteCategory, name="delete-category"),
    path("update/<str:pk>/", views.updateList, name="update"),
]
