from django.urls import path

from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('edit/<str:item_type>/<int:pk>/', views.edit_item, name='edit_item'),
]
