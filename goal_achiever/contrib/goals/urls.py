from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('edit/<str:item_type>/<int:pk>/', views.edit_item, name='edit_item'),
    path('login/', LoginView.as_view(template_name='goals/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
