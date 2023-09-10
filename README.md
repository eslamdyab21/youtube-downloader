# youtube-downloader
Download youtube playlist videos with python.

## How to use
First install packages in `requirements.txt` file

```
🢂 pip3 install -r requirements.txt
```

Then run the script
```
🢂 python3 main.py
Enter Playlist URL:
```
The script asks for playlist url, type it then enter.

```
🢂  python3 main.py 
Enter Playlist URL:
https://youtube.com/playlist?list=PLWS2mFp_C6rPXhBwR7ZpwYTjlR8HNGJGh&si=BSqrwXgS5eJm2YZz
Number of videos in the playlist: 18

Videos in the playlist
----------------------------------------------
0 -->  CURIOSITY - Featuring Richard Feynman
1 -->  TIMELAPSE OF THE FUTURE: A Journey to the End of Time (4K)
2 -->  TIMELAPSE OF THE ENTIRE UNIVERSE
3 -->  ONE SPECIES - A stirring take on climate change from Isaac Asimov
4 -->  The Discovery of Fire
5 -->  Bill Nye - The Joy of Discovery - by Melodysheep
6 -->  Our Story in 1 Minute
7 -->  What is a God?  (feat. Jason Silva)
8 -->  Escaping Earth with Morgan Freeman
9 -->  Anthropocene
10 -->  LIFE BEYOND:  Chapter 1. Alien life, deep time, and our place in cosmic history (4K)
11 -->  The Secret History of the Moon - 4K
12 -->  LIFE BEYOND II: The Museum of Alien Life (4K)
13 -->  In the Blink of an Eye:  Space in an Instant
14 -->  Let There Be Life: A Cosmic Art Loop (4K) (2x Loop)
15 -->  THE SIGHTS OF SPACE:  A Voyage to Spectacular Alien Worlds
16 -->  Has A.I. Discovered Alien Life?
17 -->  WATER WORLDS: Hideouts for Alien Life?
----------------------------------------------

Select videos you want to download...
Ex: 0,2,3,5,6,7 or all
Enter your selection:
```

The script then displays the videos titles in the playlist and asks to chose either a selected videos or all.

```
Select videos you want to download...
Ex: 0,2,3,5,6,7 or all
Enter your selection: 0,4,5,14
----------------------------------------------

Downloading started...
Video title: CURIOSITY - Featuring Richard Feynman
Video download quality: 720p
File Size: 14.49 MB
progress: 65.15%
progress: 100.0%
Download Completed
Download path: /media/ext1/eslamdyab/Documents/Projects/youtube-downloader/CURIOSITY - Featuring Richard Feynman.mp4


Downloaded: 1 out of 4
Video title: The Discovery of Fire
Video download quality: 720p
File Size: 17.2 MB
progress: 54.86%
progress: 100.0%
Download Completed
Download path: /media/ext1/eslamdyab/Documents/Projects/youtube-downloader/The Discovery of Fire.mp4


Downloaded: 2 out of 4
Video title: Bill Nye - The Joy of Discovery - by Melodysheep
Video download quality: 720p
File Size: 13.1 MB
progress: 72.04%
progress: 100.0%
Download Completed
Download path: /media/ext1/eslamdyab/Documents/Projects/youtube-downloader/Bill Nye - The Joy of Discovery - by Melodysheep.mp4


Downloaded: 3 out of 4
Video title: Let There Be Life: A Cosmic Art Loop (4K) (2x Loop)
Video download quality: 720p
File Size: 9.5 MB
progress: 99.31%
progress: 100.0%
Download Completed
Download path: /media/ext1/eslamdyab/Documents/Projects/youtube-downloader/Let There Be Life A Cosmic Art Loop (4K) (2x Loop).mp4


Downloaded: 4 out of 4
Downloading Done...

```
Here I selected 0,4,5,14 videos, and they got downloaded in the same folder where the script is.

```
🢂  ls
'Bill Nye - The Joy of Discovery - by Melodysheep.mp4'
'Let There Be Life A Cosmic Art Loop (4K) (2x Loop).mp4'
main.py     
requirements.txt
'CURIOSITY - Featuring Richard Feynman.mp4'        
LICENSE             
README.md  
'The Discovery of Fire.mp4'
```