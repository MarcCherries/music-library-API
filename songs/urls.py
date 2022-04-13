from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_song_list),
    path('<int:pk>/', views.get_song_detail),
  
]