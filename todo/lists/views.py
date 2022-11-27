from django.shortcuts import render

# Create your views here.


def lists(request):
    return render(request, "lists/home.html")


def add_list(request):
    return render(request, "lists/add.html")


def view_list(request):
    return render(request, "lists/edit.html")