# main.py
# PYTHON PROJECTS - "YT Downloader"

# Abdulqayumov Abdukarim

from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress


# Sample YouTube link: https://youtu.be/Rj_vssRaZlQ?si=lHx6ey8I3QVW_ajah
# Sample YouTube Playlist link: https://youtube.com/playlist?list=PLqwe009vcafAOnpXIR4GYLWZs49TvPbaz&si=K-YPfmiD2QnjBvEi


# --- FUNCTIONS ---

# Basic video info function
def video_info(video_url):
    yt = YouTube(video_url)
    
    # Get the organized info of video
    vhours_length = yt.length // 3600
    vminutes_length = (yt.length % 3600) // 60
    vseconds_length = yt.length % 60

    # Make video length flexible
    if vhours_length > 0:
        v_length = f"{vhours_length} hours {vminutes_length} minutes {vseconds_length} seconds"
    else:
        v_length = f"{vminutes_length} minutes {vseconds_length} seconds"

    # Show results
    print("URL TYPE:\t YT Video")
    print(f"CHANNEL:\t {yt.author}")
    print(f"TITLE:\t {yt.title}")
    print(f"LENGTH:\t {v_length}")


# Video download function
def video_download(video_url, choice):
    yt = YouTube(video_url, on_progress_callback=on_progress)
     
    v_filename = file_name_cleaning(yt.title)

    # Downloading in mp4 format with audio
    if choice == 1:
        folder = "downloads/videos"
        yt.streams.get_highest_resolution().download(output_path=folder, filename=f"{v_filename}.mp4")

        print(f"Success! Video saved into file: {v_filename}.mp4")
    # Downloading in mp3 format
    elif choice == 2:
        folder = "downloads/audios"
        yt.streams.get_audio_only().download(output_path=folder, filename=f"{v_filename}.mp3")

        print(f"Success! Audio saved into file: {v_filename}.mp3")


# Basic playlist info
def playlist_info(playlist):
    pl = Playlist(playlist)

    # Show results
    print("URL TYPE:\t\t YT Playlist")
    print(f"CHANNEL:\t\t {pl.owner}")
    print(f"TITLE:\t\t {pl.title}")
    print(f"NUMBER OF VIDEOS:\t {len(pl.video_urls)}")


# Downloading the YouTube playlist videos   
def playlist_download(playlist, choice):
    pl = Playlist(playlist)
    
    # Ask permission to download all the videos because it is the long process
    while True:
        ask = input(f"Do you want to download all the videos from playlist: {pl.title} (y/n): ")
        if ask.lower() == "y":
            break
        elif ask.lower() == "n":
            return
        else:
            print("Wrong choice! Please try again")
    
    v_playlist_name = file_name_cleaning(pl.title)
    # downloads folder with playlist file separataly 
    folder = f"downloads\playlist {v_playlist_name}"

    # Downloading in mp4 format with audio
    if choice == 1:
        for video in pl.videos:
            # File name 
            v_filename = file_name_cleaning(video.title)
        
            # downloading
            print(f"Downloading: {video.title}")
            video.streams.get_highest_resolution().download(output_path=folder, filename=f"{v_filename}.mp4")

            print(f"Success! All videos saved into file: downloads\playlist {v_playlist_name}")
    # Downloading in mp3 format
    elif choice == 2:
        for video in pl.videos:
            # File name 
            v_filename = file_name_cleaning(video.title)
        
            # downloading
            print(f"Downloading: {video.title}")
            video.streams.get_audio_only().download(output_path=folder, filename=f"{v_filename}.mp3")

            print(f"Success! All audios saved into file: downloads\playlist {v_playlist_name}")


# Function to clean the names of files and folders
def file_name_cleaning(name):
    # List of all not allowed symbols in crating the file in Windows
    not_allowed_symbols = ["\\", "/", "*", "?", ":", "<", ">", "|", "[", "]", '"']

    for char in not_allowed_symbols:
        name = name.replace(char, "")
    
    return name.strip().replace("  ", " ")

# --- START ---

print("--- YouTube Video Downloader ---")

# Create the loop
exit = True
while exit:
    # Getting url
    url_input = input("\nEnter the YouTube Video URL: ")
    
    # Basic info about video
    print("\nChecking video details...")
    # Checking for playlist
    if "list=" in url_input:
        try:
            playlist_info(url_input)
            url_type = "playlist"
        except Exception:
            print("Oops, something went wrong! Try again")
            continue
    else:
        try: 
            video_info(url_input)
            url_type = "video"
        except Exception:
            print("Oops, something went wrong! Try again")
            continue

    # Quality option
    print("\nChoose an option:")
    print("1. High Quality Video (.mp4)")
    print("2. Audio Only (.mp3)")
    choice_input = input("Selection: ")
    
    # Converting string input into integer
    try:
        choice_input = int(choice_input)
    except Exception:
        print("Wrong choice! Try again")
        continue
    
    # Downloading video in a requested form
    print("\nDownloading... Please wait.")
    if url_type == "video":
        try: 
            video_download(url_input, choice_input)
        except Exception:
            print("Oops, something went wrong! Try again")
    elif url_type == "playlist":
        try: 
            playlist_download(url_input, choice_input)
        except Exception as e:
            print("Oops, something went wrong! Try again")
    

# --- END ---