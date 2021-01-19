from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='inventory_index'),
    path('type<type_id>/', views.type, name='type'),
    path('<item_id>/', views.item, name='item')
]
