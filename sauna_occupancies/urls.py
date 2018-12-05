from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('occupancy/create-occupancy/', views.create_occupancy, name='create_occupancy'),
    path('occupancy/change/<int:occupancy_id>/', views.change_occupancy, name='change_occupancy'),
    path('occupancy/change/<int:occupancy_id>/add_user', views.add_user_to_occupancy, name='add_user_to_occupancy'),
    path('login/', auth_views.LoginView.as_view(redirect_field_name='index'), name='login'),
]
