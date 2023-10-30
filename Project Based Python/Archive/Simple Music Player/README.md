<img src="./images/music-player.png" width="700"/>

# Simple Music Player
> DIFFICULTY: **INTERMEDIATE**

In this Python project we want to create a simple music player with **pygame** and **tkinter** modules.  
We import **mixer** from pygame module to use for load, play, pause, stop, and resume the music and **tkinter** module to develop GUI.  
Also need to **os** module to access the song folder.

## TODO

1. Define *listsongs* function to create a list of all songs in the given path
2. Define *playsong* function to load the active song from the list and plays the required song. It gets executed when the user clicks on “play”.
3. Define *pausesong* function to pause the required song. It gets executed when the user clicks on “pause”.
4. Define *stopsong* function to stop the required song. It gets executed when the user clicks on “stop”.
5. Define *resumesong* function to resume the required song. It gets executed when the user clicks on “resume”.
6. Create GUI for playlist and bottons.

## Before Run

Replace the path where your songs are in following line of the program.
```python
os.chdir(r'Enter the path of your songs here')
```
## Result

Your music player should look like the image below:

<img src="./images/result.png" width="400"/>