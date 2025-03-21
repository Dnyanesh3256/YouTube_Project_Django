from django.shortcuts import render
from django.http import HttpResponse
from yt_dlp import YoutubeDL
import os

# Create your views here.

def import_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        output_folder = 'downloads'

        os.makedirs(output_folder, exist_ok=True)
        options = {
            "outtmpl": f"{output_folder,}/%(title)s.%(ext)s",
            "noplaylist": False,
        }

        try:
            with YoutubeDL(options) as ydl:
                ydl.download([url])
            return HttpResponse("Download completed successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred : {e}")
        
    return render(request, 'downloader/index.html')


