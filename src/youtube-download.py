from __future__ import unicode_literals
import yt_dlp
import sys
import typing
import os

urls = sys.argv[1:]

if len(urls) == 0:
    print("Please provide a youtube url!")
    os._exit(1)
    
ydl_opts: typing.Any = {
    "outtmpl": "%(title)s.%(ext)s",
    # "restrictfilenames": True, # replace space with _
    "ignoreerrors": True,
    "format": "mp4",
    "continuedl": True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)
