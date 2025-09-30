from django.urls import path
from AppTwo import views

urlpatterns = [
    path('',views.TaskTwo, name="tasktwo"),
    path('third/', views.TaskThree, name='third'),
    path('third/four/<int:id>/', views.TaskFour, name='four'), # if we want to pass String then use <str:name> instead of <int:id>
    path("New_Url", views.New_Url_view, name="New_Url"),
    path("Old_Url", views.Old_Url, name="Old_Url")
]