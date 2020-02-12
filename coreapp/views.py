from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item
# from django.contrib.auth.models import User


# API based views if you want that for whatever reason
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

