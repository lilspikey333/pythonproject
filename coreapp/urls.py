from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items/', views.ItemList.as_view(), name="item_list"),
    path('items/<int:pk>', views.ItemDetail.as_view(), name="item_detail"),
    # path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]