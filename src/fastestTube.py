''' A graphical interface for yt-dlp using dearpygui
    Inspired by the lack of a simple open-source youtube downloader 
    Available "free" software is fully bloated with bloatware or full
    of unnecessary things and god knows what else. created by Carlo Cattano 26/12/2021 
    https://github.com/CarloCattano  https://vueme.herokuapp.com/#/     ''' 

import dearpygui.dearpygui as dpg  #requires ffmpeg in PATH or binary in the same folder
from yt_dlp import YoutubeDL

dpg.create_context()
dpg.create_viewport(width=600, height=500,resizable=False,title="Fastest Tube", small_icon="resources/tube.ico",large_icon="resources/tube.ico")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_global_font_scale(1)

vidURL = ""
dInfo = ""

class MyLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        if msg.startswith('[download]'):
            msg = msg[11:]
            pConsole(msg)

        if msg.startswith('[ExtractAudio]'):
            msg = msg[14:]
            pConsole("Encoding...")
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pConsole("ERROR - wrong URL?? ")


def my_hook(d):
    if d['status'] == 'finished':
        pConsole("Finished")

pBuffer = []

def pConsole(c):
    global pBuffer
    pBuffer.append(c)

    if len(pBuffer) > 20:
        pBuffer.pop(0)
    dpg.set_value("dConsole",value="\n".join(pBuffer))

def dl_audio():
    global vidURL,info

    ydl_opts = {'format': 'bestaudio' , 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',}],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    if  dpg.get_value(item="dConsole") == "dconsole":
        pConsole("URL cant be empty!")

    else:
        with YoutubeDL(ydl_opts) as ydl:

            if "list" not in vidURL:    
                ydl.download([vidURL])
                print("NOT A PLAYLIST")

            if "list" in vidURL:               
                # folder = dpg.add_file_dialog(directory_selector=True,file_count=8)
                info = ydl.extract_info(vidURL, download=False)
                print(info['title'])
                ydl.download([vidURL])

def dl_video():
    global vidURL
    if aPlusVideo is True:
        ydl_opts = {'format': 'bestvideo+bestaudio/best[ext=mp4]','logger': MyLogger(),
                            'progress_hooks': [my_hook]}
    else:
        ydl_opts = {'format': 'bestvideo[ext=mp4]','logger': MyLogger(),
                                'progress_hooks': [my_hook]}

    if  dpg.get_value(item="dConsole") == "dconsole":
        pConsole("URL cant be empty!")

    else:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([vidURL])

aPlusVideo = False

def setURL(sender,data):
    global vidURL
    vidURL = data

def vidSetAV():
    global aPlusVideo
    aPlusVideo = not aPlusVideo

with dpg.window(tag="Primary Window",label="URL :",no_collapse=True,width=600,height=600,no_close=True,no_resize=True,no_move=True):   
    dpg.add_input_text(width=500,height=50,callback=setURL)
    dpg.add_button(label="Download Audio",width=180,height=40,callback=dl_audio)
    dpg.add_button(label="Download Video",width=180,height=40,callback=dl_video)
    #add dpg checkbox for audio+video
    dpg.add_checkbox(label="Audio+Video",callback=vidSetAV,pos=(200,114))

    with dpg.group(horizontal=True):
        dpg.add_text("Info",tag="dConsole")

dpg.start_dearpygui()
dpg.destroy_context()