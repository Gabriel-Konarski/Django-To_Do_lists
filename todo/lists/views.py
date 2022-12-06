from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from .models import Category, List, Item
# Create your views here.


def lists(request):
    category = request.GET.get('category')
    user = request.user

    if category is None:
        all_lists = List.objects.filter(category__user=user)
    else:
        all_lists = List.objects.filter(category__user=user, category__name=category)

    categories = Category.objects.filter(user=user)
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

        request.user.category_set.add(category)

        return redirect('lists')

    context = {'categories': categories}
    return render(request, "lists/add.html", context)


def userDetail(request):
    user = request.user
    lists = List.objects.filter(category__user=user)
    categories = Category.objects.filter(user=user)
    context = {'lists': lists, 'categories': categories}

    return render(request, "lists/user.html", context)


def deleteList(request, pk):
    lista = get_object_or_404(List, id=pk)
    context = {"lista": lista}

    if request.method == "POST":
        lista.delete()

        return HttpResponseRedirect("/")

    return render(request, "lists/delete.html", context)


def deleteItem(request, pk):
    item = get_object_or_404(Item, id=pk)
    context = {"item": item}

    if request.method == "POST":
        item.delete()

        return HttpResponseRedirect("/")

    return render(request, "lists/delete.html", context)


def deleteCategory(request, pk):
    category = get_object_or_404(Category, id=pk)
    context = {'category': category}

    if request.method == "POST":
        category.delete()

        return redirect('account')

    return render(request, "lists/delete.html", context)
