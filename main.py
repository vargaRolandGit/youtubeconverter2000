from pytube import YouTube
import os
import PySimpleGUI as sg
import ffmpeg

def on_complete_audio(stream,file_path):
    pass

def on_complete(stream,file_path):
    print('complete')

def on_progress(stream,chunk,bytes_remaining):
    print(f"{100-(round(bytes_remaining / stream.filesize * 100))}%")

video_object = YouTube(
    'https://www.youtube.com/watch?v=3vSxHROQ4Hs',
    on_complete_callback = on_complete,
    on_progress_callback = on_progress,)

audio_object = YouTube(
    'https://www.youtube.com/watch?v=3vSxHROQ4Hs',
    on_complete_callback = on_complete_audio)

#print(video_object.streams)
video = video_object.streams.get_by_itag(271).download()
os.rename(video, "video.mp4")
audio = audio_object.streams.get_audio_only().download()
os.rename(audio, "audio.mp4")

input_video = ffmpeg.input('video.mp4')
input_audio = ffmpeg.input('audio.mp4')

(
    ffmpeg
    .concat(input_video, input_audio, v=1, a=1)
    .output("./done/output.mp4")
    .run(overwrite_output=True)
)

print("done")