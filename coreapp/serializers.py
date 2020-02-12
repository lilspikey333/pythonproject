from rest_framework import serializers
# from django.contrib.auth.models import User

from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user.id')
    class Meta:
        model = Item
        fields = ('id', 'category', 'title', 'image', 'description', 'price', 'condition', 'top_size', 'bottom_size', 'shoe_size',)

    # def create(self, validated_data):
    #     Item = Item.objects.create(
    #         category = validated_data['category'],
    #         title = validated_data['title'],
    #         image = validated_data['image'],
    #         description = validated_data['description'],
    #         price = validated_data['price'],
    #         condition = validated_data['condition'],
    #         top_size = validated_data['top_size'],
    #         bottom_size = validated_data['bottom_size'],
    #         shoe_size = validated_data['shoe_size'],
    #     )
    #     return item