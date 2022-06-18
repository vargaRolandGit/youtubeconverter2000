import PySimpleGUI as sg

layout = [[sg.Text('Text'),sg.Spin(['item','item2'])],
          [sg.Button('Button')],
          [sg.Input()],
          [sg.Text('URL:'),sg.Button('Convert')]]
sg.Window('Youtube Converter 2000',layout).read()

