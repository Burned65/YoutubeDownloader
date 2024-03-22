import tkinter.ttk

import yt_dlp
#import PySimpleGUI as Sg
from tkinter import *
from tkinter.ttk import *
import os


"""
def download(x, y, z):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': f'{z}',
            'preferredquality': '192',
        }],
        'outtmpl': x + "/" + y
    }
    url = values["-URL-"]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    Sg.popup("Video fertig heruntergeladen!")
    window['-URL-']('')
    window['-TITLE-']('')


def download_video(x, y):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': x + "/" + y
    }
    url = values["-URL-"]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    Sg.popup("Video fertig heruntergeladen!")
    window['-URL-']('')
    window['-TITLE-']('')


if __name__ == '__main__':
    layout = [
        [
            Sg.Text("Speicherort", size=(8, 1)),
            Sg.InputText(size=(25, 1), key="-FOLDER-"),
            Sg.FolderBrowse()
        ],
        [
            Sg.Text("Video-URL", size=(8, 1)),
            Sg.InputText(size=(25, 1), key="-URL-"),
            Sg.Combo(['mp3', 'm4a', 'wav', 'mp4'], key="-FORMAT-")
        ],
        [
            Sg.Text("Titel", size=(8, 1)),
            Sg.InputText(size=(25, 1), key="-TITLE-"),
        ],
        [
            Sg.Text("", size=(8, 1)),
            Sg.Button("Beenden"),
            Sg.Button("Download")
        ]
    ]

    window = Sg.Window("Youtube Download", layout)

    while True:
        event, values = window.read()

        if event == "Download":
            if values["-FORMAT-"] == "mp4":
                try:
                    path = values["-FOLDER-"]
                    title = values["-TITLE-"]
                    if os.path.isfile(path + "/" + title + ".mp4"):
                        if Sg.popup_yes_no("Datei existiert bereits, überschreiben?") == "Yes":
                            os.remove(path + "/" + title + ".mp4")
                            download_video(path, title)
                    else:
                        download_video(path, title)
                except yt_dlp.utils.DownloadError:
                    Sg.popup("Etwas ist schiefgelaufen :(\nWahrscheinlich wurde der Videolink nicht gefunden!",
                             no_titlebar=True, background_color="darkblue")
            else:
                try:
                    file_format = values["-FORMAT-"]
                    path = values["-FOLDER-"]
                    title = values["-TITLE-"]
                    if file_format == "":
                        file_format = "mp3"
                    if os.path.isfile(path + "/" + title + f".{file_format}"):
                        if Sg.popup_yes_no("Datei existiert bereits, überschreiben?") == "Yes":
                            os.remove(path + "/" + title + f".{file_format}")
                            download(path, title, file_format)
                    else:
                        download(path, title, file_format)
                except yt_dlp.utils.DownloadError:
                    Sg.popup("Etwas ist schiefgelaufen :(\nWahrscheinlich wurde der Videolink nicht gefunden!",
                             no_titlebar=True, background_color="darkblue")

        if event == "Beenden":
            if Sg.popup_yes_no("Wirklich Beenden?") == "Yes":
                break

        if event == Sg.WIN_CLOSED:
            break

    window.close()
"""


def download():
    print(path.get())
    print(url.get())
    print(title.get())
    print(download_type.get())


def stop():
    popup = Toplevel(root)
    popup.title("Wirklich Beenden?")

    Button(popup, text="Ja", command=root.destroy()).grid(column=1, row=1)
    Button(popup, text="Nein", command=popup.destroy()).grid(column=2, row=1)


if __name__ == '__main__':
    root = Tk()
    root.title("YoutubeDownloader")
    mainframe = Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    Label(mainframe, text="Speicherort").grid(column=1, row=1)
    path = StringVar()
    Entry(mainframe, textvariable=path).grid(column=2, row=1)
    Button(mainframe, text="Browse").grid(column=3, row=1)

    Label(mainframe, text="Video-Url").grid(column=1, row=2)
    url = StringVar()
    Entry(mainframe, textvariable=url).grid(column=2, row=2)
    download_type = StringVar()
    Combobox(mainframe, textvariable=download_type, values=['mp3', 'm4a', 'wav', 'mp4']).grid(column=3, row=2)

    Label(mainframe, text="Titel").grid(column=1, row=3)
    title = StringVar()
    Entry(mainframe, textvariable=title).grid(column=2, row=3)
    Button(mainframe, text="Download", command=download).grid(column=3, row=3)

    Button(mainframe, text="Beenden", command=stop).grid(column=3, row=4)

    root.mainloop()
