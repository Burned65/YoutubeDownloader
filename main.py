import yt_dlp
import PySimpleGUI as Sg
import os


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
