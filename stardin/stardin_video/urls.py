from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page',),
    path('login', views.login, name='login'),
    path('videos', views.videos, name='videos'),
    path('video/<uuid:video_id>/', views.video, name='video'),
    path('player/<uuid:video_id>/', views.video_player, name='player'),
]