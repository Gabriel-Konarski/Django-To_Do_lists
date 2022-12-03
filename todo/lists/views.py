from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from .models import Category, List, Item
# Create your views here.


def lists(request):
    category = request.GET.get('category')

    if category is None:
        all_lists = List.objects.all()
    else:
        all_lists = List.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {"categories": categories, "all_lists": all_lists}

    return render(request, "lists/home.html", context)


def viewList(request, pk):
    lista = List.objects.get(id=pk)
    items = lista.item_set.all()

    if request.method == "POST":
        if request.POST.get("newItem"):
            data = request.POST

            if len(data['item']) > 2:
                new_item = Item.objects.create(
                    lists=lista,
                    name=data['item'],
                    complete=False,
                )
            else:
                print("invalid")

        elif request.POST.get("save"):
            for item in items:
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

    context = {"lista": lista, "items": items}

    return render(request, "lists/edit.html", context)


def addList(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data["category_new"] != '':
            category, created = Category.objects.get_or_create(name=data["category_new"])
        else:
            category = None

        lista = List.objects.create(
            category=category,
            name=data['name'],
        )

        return redirect('lists')

    context = {'categories': categories}
    return render(request, "lists/add.html", context)


def deleteList(request, pk):
    lista = get_object_or_404(List, id=pk)
    context = {"lista": lista}

    if request.method == "POST":
        lista.delete()

        return HttpResponseRedirect("/")

    return render(request, "lists/delete.html", context)
