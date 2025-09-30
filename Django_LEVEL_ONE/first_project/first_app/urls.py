from django.urls import path
from first_app import views

urlpatterns =[
    path('index/', views.Index, name="Index"),
    path('', views.Home, name="help"),
]