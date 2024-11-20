import os
import subprocess

import yt_dlp


# Function to download a single song
def download_song(query, output_dir="downloads"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Searching and downloading: {query}")
            ydl.download([f"ytsearch:{query}"])
    except Exception as e:
        print(f"Failed to download {query}: {e}")

# Read songs from the text file and download them
def download_songs_from_file(file_path, output_dir="downloads"):
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist!")
        return
    with open(file_path, 'r') as f:
        songs = [line.strip() for line in f if line.strip()]
    for song in songs:
        download_song(song, output_dir)

if __name__ == "__main__":
    # Replace 'songs.txt' with the path to your file
    song_list_file = "songs.txt"
    download_songs_from_file(song_list_file)
