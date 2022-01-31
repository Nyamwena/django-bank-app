from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('customer_details/<str:pk>/', views.view_details, name="details"),

]