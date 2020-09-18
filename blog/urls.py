from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostsList.as_view(), name='post_list' ),
]