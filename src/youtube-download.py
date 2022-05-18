from __future__ import unicode_literals
import yt_dlp
import sys
import typing
import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--audio', '-a', action='store_true', help='download audio')
    args = parser.parse_args()
    
    ydl_opts: typing.Dict = {}
    
    if args.audio:        
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            # "restrictfilenames": True, # replace space with _
            "ignoreerrors": True,
            "format": "bestaudio/best",
            "continuedl": True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    else:
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            # "restrictfilenames": True, # replace space with _
            "ignoreerrors": True,
            "format": "mp4",
            "continuedl": True
        }
        
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    
    if not sys.stdin.isatty():
        for line in sys.stdin:
            if line == "\n": continue

            url = line.strip()
            ydl.download(url)
    else:
        while True:
            url = input("\u001b[33;1m[URL]\u001b[0m ")
            if url == "quit" or url == "q" or url == "exit" or url == "e": break
            
            ydl.download(url)

if __name__ == '__main__':
    main()