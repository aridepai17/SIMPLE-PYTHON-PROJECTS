from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloadyoutubevideo(url, savepath):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highestresstream = streams.get_highest_resolution()
        highestresstream.download(output_path = savepath)
        print("Download Successful")
    except Exception as e:
        print(e)
        
def openfiledialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    url = input("Enter YouTube video URL: ")
    savepath = openfiledialog()
    
    if savepath:
        print("Downloading...")
        downloadyoutubevideo(url, savepath)
    else:
        print("Invalid path selected.")
    
        