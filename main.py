import os
from downloader.downloader import fetch_video_info, download_audio
from downloader.metadata import add_id3_tags
from downloader.utils import sanitize_filename

COOKIE_FILE = 'youtube_cookies.txt'
FFMPEG_PATH = os.path.abspath('C:/Users/apgra/Desktop/YouTToMp3/tools/ffmpeg-win-x86_64-v7.1.exe')

def download_audio_as_mp3(query):
    info = fetch_video_info(query, COOKIE_FILE)
    title_clean = sanitize_filename(info.get('title', 'audio_output'))
    artist_clean = sanitize_filename(info.get('uploader', 'Unknown Artist'))

    print(f'🎧 Название: {title_clean}')
    print(f'👤 Артист: {artist_clean}')

    download_audio(query, title_clean, FFMPEG_PATH, COOKIE_FILE)
    add_id3_tags(f'{title_clean}.mp3', title_clean, artist_clean)

if __name__ == '__main__':
    download_audio_as_mp3("Imagine Dragons Believer")