from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='project_index'),
    path('<project_id>/', views.project, name='project')
]
