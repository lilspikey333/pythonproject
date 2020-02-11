from django.shortcuts import render, redirect
# from rest_framework import generics
# from .serializers import ItemSerializer
from .models import Item
from django.contrib.auth.models import User
from .forms import ItemForm
from django.contrib.auth.decorators import login_required


# API based views if you want that for whatever reason
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()

# class ItemList(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'core/item_detail.html', {'item': item})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            print(request.user.id)
            item.user_id = request.user.id
            item.save()
            return redirect('item_detail', pk = item.id)
    else:
        form = ItemForm()
    return render(request, 'core/item_form.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/item_form.html', {'form': form})

@login_required
def item_delete(request, pk):
    Item.objects.get(id=pk).delete()
    return redirect('item_list')

