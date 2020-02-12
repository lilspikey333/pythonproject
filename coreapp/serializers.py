from rest_framework import serializers
# from django.contrib.auth.models import User

from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user.id')
    class Meta:
        model = Item
        fields = ('id', 'category', 'title', 'image', 'description', 'price', 'condition', 'top_size', 'bottom_size', 'shoe_size',)