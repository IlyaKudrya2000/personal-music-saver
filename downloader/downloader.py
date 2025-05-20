import yt_dlp
from .utils import sanitize_filename

def fetch_video_info(query, cookie_path, quiet=True):
    with yt_dlp.YoutubeDL({'quiet': quiet, 'cookiefile': cookie_path}) as ydl:
        info = ydl.extract_info(f'ytsearch1:{query}', download=False)
        return info['entries'][0] if 'entries' in info else info

def download_audio(query, filename, ffmpeg_path, cookie_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{filename}.%(ext)s',
        'default_search': 'ytsearch1',
        'noplaylist': True,
        'quiet': False,
        'cookiefile': cookie_path,
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': ['-ar', '44100'],
        'prefer_ffmpeg': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])