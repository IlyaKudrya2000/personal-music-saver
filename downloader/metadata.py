from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def add_id3_tags(filename, title, artist):
    try:
        audio = MP3(filename, ID3=EasyID3)
        audio['title'] = title
        audio['artist'] = artist
        audio.save()
        print(f"✅ ID3-теги добавлены: {filename}")
    except Exception as e:
        print(f"⚠️ Не удалось добавить теги: {e}")