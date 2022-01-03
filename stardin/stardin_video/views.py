from django.shortcuts import render
from django.http import HttpResponse

from .models import Video, Episode_Data

def index(request):
    return HttpResponse("Hello, world. You're at the stardin_video index.")

def main_page(request):
    videos = Video.objects.all

    context = {
        'videos': videos,
    }
    response = render(request, 'main_page.html', context)
    response.set_cookie('QWERTY', 'Testing')
    return response

def video(request, video_id):
    video = Video.objects.get(uuid=video_id)

    context = {
        'video': video,
    }
    return render(request, 'video.html', context)

def video_player(request, video_id):
    video = Video.objects.get(uuid=video_id)

    context = {
        'video': video,
    }
    return render(request, 'player.html', context)