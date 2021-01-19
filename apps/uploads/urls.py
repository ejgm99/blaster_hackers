from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='upload_index'),
    path('inventory/', views.inventory, name = 'inventory'),
    path('components/', views.components, name = 'components')
]
