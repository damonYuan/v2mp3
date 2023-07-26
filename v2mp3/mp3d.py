from pytube import YouTube
import os
import subprocess
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

_filename = str(input("Enter the filename: \n>> ")) or str(yt.title)
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination, filename=f"{_filename}.mp4")
  
# save the file
base, ext = os.path.splitext(out_file)
original = base + '.mp4'
mp3 = _filename + '.mp3'
ffmpeg = ('ffmpeg -i %s ' % original + mp3)
print(ffmpeg)
subprocess.call(ffmpeg, shell=True)
  
# result of success
print(_filename  + " has been successfully downloaded.")
os.remove(original)
