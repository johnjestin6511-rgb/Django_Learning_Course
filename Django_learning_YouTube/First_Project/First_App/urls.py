from django.urls import path
from First_App import views

app_name = 'First'

urlpatterns =[
    path('', views.index, name = 'index'),
    path('post/<str:id>/', views.details, name = 'details'),
    path('new-url/', views.new_url_view, name = 'new_page_url'),
    path('old-url/', views.old_url_redirect, name = 'old_url'),
    # path('html-page/', views.Html_page, name = 'html_page')
]