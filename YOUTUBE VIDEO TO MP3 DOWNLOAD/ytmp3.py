import os
from pytube import YouTube
from moviepy.editor import *

def downloadmp3(youtubeurl, outputpath):
    try:
        yt = YouTube(youtubeurl)
        audiostream = yt.streams.filter(only_audio = True).first()
        print(f"Downloading {yt.title}...")
        audiofile = audiostream.download(output_path = outputpath, filename="tempaudio.mp4")
        
        print(f"Converting to MP3: {yt.title}...")
        audio_clip = AudioFileClip(os.path.join(outputpath, "tempaudio.mp4"))
        mp3file = os.path.join(outputpath, yt.title + ".mp3")
        audio_clip.write_audiofile(mp3file, codec='mp3')
        audio_clip.close()
        
        os.remove(os.path.join(outputpath, "tempaudio.mp4"))  # Remove the temporary audio file
        
        print(f"Download and conversion complete: {mp3file}")
        return mp3file
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        youtubeurl = input("Enter YouTube URL: ").strip()
        if not youtubeurl:
            print("YouTube URL cannot be empty. Please enter a valid URL.")
            continue
        if not ("youtube.com" in youtubeurl or "youtu.be" in youtubeurl):
            print("Invalid URL. Please enter a valid YouTube URL.")
            continue
        break
    
    while True:
        outputpath = input("Enter output path: ").strip()
        if not outputpath:
            print("Output path cannot be empty. Please enter a valid path.")
            continue
        if not os.path.exists(outputpath):
            try:
                os.makedirs(outputpath)
                print(f"Output path created: {outputpath}")
            except Exception as e:
                print(f"An error occurred while creating the output path: {e}")
                continue
        print(f"Output path set to: {outputpath}")
        break
    
    downloadmp3(youtubeurl, outputpath)
