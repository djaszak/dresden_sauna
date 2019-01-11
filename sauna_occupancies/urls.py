from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.occupancy_calendar, name='occupancy_calendar'),
    path('occupancy/create-occupancy/', views.create_occupancy, name='create_occupancy'),
    path('occupancy/change/<int:occupancy_id>/', views.change_occupancy, name='change_occupancy'),
    path('occupancy/change/<int:occupancy_id>/add_user/', views.add_user_to_occupancy, name='add_user_to_occupancy'),
    path('occupancy/list/<int:year>/<int:month>/<int:day>/', views.occupancy_list, name='occupancy_list'),
    path('login/', auth_views.LoginView.as_view(redirect_field_name='occupancy_calendar'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('csv-download/', views.csv_download, name='csv_download')
]
