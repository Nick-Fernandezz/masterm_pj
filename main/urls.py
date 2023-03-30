from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # re_path(r'^1?/', views.index_front),
    # re_path(r'^2?/', views.index_main),
]
