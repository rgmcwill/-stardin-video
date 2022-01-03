from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('video/<uuid:video_id>/', views.video, name='video'),
    path('player/<uuid:video_id>/', views.video_player, name='player'),
]