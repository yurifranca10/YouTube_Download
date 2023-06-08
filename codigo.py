from pytube import YouTube 
import os

url = "https://www.youtube.com/watch?v=m2TIIJvW-xk&ab_channel=detonautasVEVO"


yt = YouTube(url)



### Download formato .mp4 (video) do youtube ###

video = yt.streams.get_highest_resolution()
video.download()



### Download formato .mp3 (musica) do youtube ###

audio = yt.streams.filter(only_audio=True).first()
out_file = audio.download()
##salvando arquivo formato .mp3 ###
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file,new_file)
## retorno para confirmação ## 
print(yt.title + "has been successfully download.")