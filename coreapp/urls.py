from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('items/', views.ItemList.as_view(), name="item_list"),
#     path('items/<int:pk>', views.ItemDetail.as_view(), name="item_detail")
#     path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
# ]

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),
    path('items/new', views.item_create, name='item_create'),
    path('items/<int:pk>/edit', views.item_edit, name='item_edit'),
    path('items/<int:pk>/delete', views.item_delete, name='item_delete'),
]