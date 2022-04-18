# Fastest youtube audio / video Downloader
uses **[dearpygui](https://pypi.org/project/dearpygui/#dear-pygui)** and **[yt_dlp](https://pypi.org/project/yt-dlp/)** . **[ffmpeg](https://ffmpeg.org/)** for encoding

![image](https://user-images.githubusercontent.com/17380530/147417071-0b75581f-d40f-4a3d-bfc7-0738694248ad.png)


### features:
* Ultra Fast 
* Download video or audio at the best quality available converted to mp4 with ffmpeg
* Download entire playlists
* Download Video with or witout the audio
### to do's:
   * Add a loading/waiting.. Visual feedback after download button is pressed
   * Add a finished mesagge after encoding is done
   * Make a better UI
   * Choose ouput folder and name with default to video Title and current folder
   * create automatic fading for songs between playlists
   * learn python best practices
   * ~~learn how to use gh Actions CI to create the binaries insted of compiling them locally~~
   * ~~try to create binaries for windows and mac OSX and add to Releases~~
   * ~~Download entire playlists~~
   * ~~Implement community Feature requests like(Download Video without audio)~~ 


### Instructions:
uses python3 , so use python or python3 | pip or pip3 dependig on your configuration.
   ```bash
      pip install dearpygui yt-dlp ffmpeg
      python fastestTube.py
   ```
   (ffmpeg from pip untested , I downloaded the binaries from the offitial website for windows)

**Contributions**  such as **improvements** and **feature requests** are welcomed
