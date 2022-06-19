import PySimpleGUI as sg
from pytube import YouTube
import os
import PySimpleGUI as sg
import ffmpeg

sg.theme('SystemDefault1')
#start_layout = [[sg.Input(key='-input-'),sg.Button('Load', key = '-load-')]]
layout = [
    #[sg.Text('Youtube Converter 2000', font='Comic 10'),sg.Push(),sg.Image('close.png',enable_events=True,key='-close-')],
    [sg.VPush()],
    [sg.Text('URL:',font='Roboto 8'),sg.Input(key='-input-'),
     sg.Button('Load', key = '-load-',button_color=('#ffffff','#000000'''), border_width = 0)],
    [sg.Text('',key = '-title-',font='Roboto 12 bold')],
    [sg.Text('',key = '-author-',font='Roboto 10')],
    [sg.Text('')],
    [sg.Button('Download',key = '-download-',button_color=('#ffffff','#000000'''), border_width = 0,visible=False)],
    [sg.VPush()]
        ]
window = sg.Window('Youtube Converter 2000',
                   layout,
                   finalize=True,
                   size=(500, 300),
                   element_justification='center',
                   #no_titlebar = True
                   )
url = ''

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-close-':
        break

    if event == '-load-':
        url = values['-input-']
        video_object = YouTube(url)
        audio_object = YouTube(url)


        #video info
        window['-title-'].update(video_object.title)
        window['-author-'].update(f'from: {video_object.author}')
        window['-download-'].update(visible=True)

    if event == '-download-':
        if os.path.exists("video.mp4"):
            os.remove("video.mp4")
        if os.path.exists("audio.mp4"):
            os.remove("audio.mp4")
        video = video_object.streams.get_by_itag(313).download()
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
        print('Done')

window.close()

