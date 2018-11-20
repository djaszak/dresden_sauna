from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('occupancy/create-occupancy/', views.create_occupancy, name='create_occupancy'),
    path('occupancy/change/<int:occupancy_id>', views.change_occupancy, name='change_occupancy')
]