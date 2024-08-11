import pytube
from tkinter import messagebox
import os
# import earthpy as et
# Home = et.io.HOME
# saveToFile = Home + '\Downloads'
# saveFiles = os.path.join(saveToFile)
# saveFile = os.chdir(saveFiles)
# saveFile

# def SaveFile(FileName):
#     Home = et.io.HOME
#     saveToFile = Home + '\Downloads\\' + FileName
#     saveFiles = os.path.join(saveToFile)
    
    
    # try:
    #     os.mkdir(saveFiles)
    # except OSError as error: 
    #     pass  
    # os.chdir(saveFiles)
    # show = print(os.getcwd())
    # show


def video(dowlink):
    # SaveFile("YTVidoes")
    
    # saveFile = os.chdir(saveFiles)
    # if not saveFile:
    #     os.mkdir(saveFile)
    # else:
    #     saveFile
    try:
        yt = pytube.YouTube(dowlink)
        Stream = yt.streams.filter(progressive=True,file_extension='mp4').last()
        try:
            Stream.download()
            messagebox._show("Done","Video is downloaded")
        except Exception as down:
                messagebox.showerror("error","Can't connect to Net")
    except Exception as link:
        messagebox.showerror("error",'Enter a correct Link')

def Playlist(downlink):
    # SaveFile("YTPlaylist")
    try:
        yt = pytube.Playlist(downlink)
        for videos in yt.videos:
            try:
                videos.streams.filter(progressive=True,file_extension='mp4').last().download()
            except Exception as down:
                messagebox.showerror("error","Can't connect to Net")
        messagebox._show("Done","Playlist is downloaded")
    except Exception as link:
        messagebox.showerror("error",'Enter a correct Link')

if __name__ == "__main__":
    # SaveFile("Hello")
    while True:
        opt = int(input('''
                        1: Video
                        2: Playlist
                        3: Exit
                        '''))
        url = input("enter Url")
        if opt == 1:
            video(url)
        elif opt == 2:
            Playlist(url)
        elif opt == 3:
            False
        else:
            continue