from django.urls import path 
from . import views

urlpatterns = [
    path('categories', views.CategoryView.as_view()),
    # path('menu-items'),
    # path('menu-items/<int:pk>'),
]