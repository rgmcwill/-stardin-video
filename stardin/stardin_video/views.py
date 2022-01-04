import requests

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Video, Episode_Data

def main_page(request):
    return HttpResponse("<a href='login'>Login</a>")

def login(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('videos')

        else:
            return HttpResponse('User Not Found!')
    elif request.method == 'GET':
        return render(request, 'login.html')
    return HttpResponse("Was not a GET or POST request")

# @login_required
def videos(request):
    print(request.headers)
    videos = Video.objects.all

    context = {
        'videos': videos,
    }
    response = render(request, 'main_page.html', context)
    response.set_cookie('QWERTY', 'Testing')
    print(response.headers)
    return response

# @login_required
def video(request, video_id):
    video = Video.objects.get(uuid=video_id)

    context = {
        'video': video,
    }
    return render(request, 'video.html', context)

# @login_required
def video_player(request, video_id):
    video = Video.objects.get(uuid=video_id)

    context = {
        'video': video,
    }
    return render(request, 'player.html', context)