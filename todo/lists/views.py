from django.shortcuts import render

# Create your views here.


def lists(request):
    return render(request, "lists/home.html")


def addList(request):
    return render(request, "lists/add.html")


def viewList(request):
    return render(request, "lists/edit.html")