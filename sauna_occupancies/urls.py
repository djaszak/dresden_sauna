from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('occupancy/create-occupancy/', views.create_occupancy, name='create_occupancy')
]