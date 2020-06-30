from __future__ import unicode_literals
import youtube_dl

def download_youtube_song(url):
    ydl_opts = {'format': 'bestaudio/best',
                'noplaylist': True,
                'preferredcodec': 'mp3',
                'outtmpl': 'C:/Users/August/Desktop/stream/downloads/%(extractor_key)s/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(url)
        if not "youtube.com" in url: 
            return "ээээээээээээ"
        info = ydl.extract_info(url, download=False)
        duration = info.get("duration", None)
        if duration > 300: 
            return "ээээээээээээ"
        ydl.download([url])
