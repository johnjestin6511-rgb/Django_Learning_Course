from django.urls import path
from first_app import views

urlpatterns =[
    path('',views.index,name='index'),
    path('first_app/',views.index,name='index'),
    path('User/',views.user, name='user'),
]