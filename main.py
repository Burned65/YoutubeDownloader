import tkinter.ttk
import tkinter

import yt_dlp
from tkinter import *
from tkinter.ttk import *
import os
from tkinter import filedialog


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


def remove_and_close():
    os.remove(path.get() + "/" + title.get() + "." + download_type.get())


def download():
    try:
        if url.get() == "" or path.get() == "" or title.get() == "" or download_type.get() == "":
            popup = Toplevel(root)
            popup.title("Etwas ist schiefgelaufen")
            popup.resizable(width=False, height=False)
            popup.grab_set()

            popup_frame = Frame(popup)
            popup_frame.grid(column=0, row=0)

            Label(popup_frame, text="Eins der Pflichtfelder ist nicht gefüllt!").grid(column=1, row=1)
            Button(popup_frame, text="Ok", command=popup.destroy).grid(column=1, row=2)

            popup.geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()))

            root.wait_window(popup)

            return
        if os.path.isfile(path.get() + "/" + title.get() + "." + download_type.get()):
            popup = Toplevel(root)
            popup.title("Datei exisitiert bereits")
            popup.resizable(width=False, height=False)
            popup.grab_set()

            popup_frame = Frame(popup)
            popup_frame.grid(column=0, row=0)

            Label(popup_frame, text="Datei existiert bereits, überschreiben?").grid(column=1, row=1, columnspan=2)
            Button(popup_frame, text="Ja", command=remove_and_close).grid(column=1, row=2)
            Button(popup_frame, text="Nein", command=popup.destroy).grid(column=2, row=2)

            popup.geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()))

            root.wait_window(popup)

        if download_type.get() == "mp4":
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': path.get() + "/" + title.get()
            }
        else:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': f'{download_type.get()}',
                    'preferredquality': '192',
                }],
                'outtmpl': path.get() + "/" + title.get()
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url.get()])
        popup = Toplevel(root)
        popup.title("Video fertig heruntergeladen")
        popup.resizable(width=False, height=False)
        popup.grab_set()

        popup_frame = Frame(popup)
        popup_frame.grid(column=0, row=0)

        Label(popup_frame, text="Video wurde fertig heruntergeladen!").grid(column=1, row=1)
        Button(popup_frame, text="Ok", command=popup.destroy).grid(column=1, row=2)

        popup.geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()))

        root.wait_window(popup)

        url.set("")
        title.set("")
    except yt_dlp.utils.DownloadError as e:
        popup = Toplevel(root)
        popup.title("Etwas ist schiefgelaufen")
        popup.resizable(width=False, height=False)
        popup.grab_set()

        popup_frame = Frame(popup)
        popup_frame.grid(column=0, row=0)

        Label(popup_frame, text="Etwas ist schiefgelaufen :(\nWahrscheinlich wurde der Videolink nicht gefunden!").grid(column=1, row=1)
        Button(popup_frame, text="Ok", command=popup.destroy).grid(column=1, row=2)

        popup.geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()))

        root.wait_window(popup)


def stop():
    popup = Toplevel(root)
    popup.title("Wirklich Beenden?")
    popup.resizable(width=False, height=False)
    popup.grab_set()

    popup_frame = Frame(popup)
    popup_frame.grid(column=0, row=0)

    Label(popup_frame, text="Wirklich Beenden?").grid(column=1, row=1, columnspan=2)
    Button(popup_frame, text="Ja", command=root.destroy).grid(column=1, row=2)
    Button(popup_frame, text="Nein", command=popup.destroy).grid(column=2, row=2)

    popup.geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()))

    root.wait_window(popup)


def browse_files():
    path.set(filedialog.askdirectory(title="Speicherordner auswählen"))


if __name__ == '__main__':
    root = Tk()
    root.title("YoutubeDownloader")
    mainframe = Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(width=False, height=False)

    Label(mainframe, text="Speicherort").grid(column=1, row=1)
    path = StringVar()
    Entry(mainframe, textvariable=path).grid(column=2, row=1)
    Button(mainframe, text="Browse", command=browse_files).grid(column=3, row=1)

    Label(mainframe, text="Video-Url").grid(column=1, row=2)
    url = StringVar()
    Entry(mainframe, textvariable=url).grid(column=2, row=2)
    download_type = StringVar()
    Combobox(mainframe, textvariable=download_type, values=['mp3', 'm4a', 'wav', 'mp4'], width=8).grid(column=3, row=2)

    Label(mainframe, text="Titel").grid(column=1, row=3)
    title = StringVar()
    Entry(mainframe, textvariable=title).grid(column=2, row=3)
    Button(mainframe, text="Download", command=download).grid(column=3, row=3)

    Button(mainframe, text="Beenden", command=stop).grid(column=3, row=4)

    root.mainloop()
