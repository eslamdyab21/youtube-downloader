from pytube import YouTube
from pytube import Playlist
import requests

#Gives download progress
def on_progress(stream, chunk, bytes_remaining):
    progress = f"{round(100 - (bytes_remaining/stream.filesize * 100),2)}%"
    print(f"progress: {progress}")

#Do this on download completion
def on_complete(stream, file_path):
    print("Download Completed")
    print(f"Download path: {file_path}")


def get_playlist_titles(url):
    # request web page
    resp = requests.get(url)

    # get the response text. in this case it is HTML
    html = resp.text

    i = html.find('"title":{"runs":[{"text":')

    titles_html = html[i:]

    titles_indexes = [i for i in range(len(titles_html)) if titles_html.startswith('"title":{"runs":[{"text":', i)]

    i = 0
    for index in titles_indexes:
        if 'accessibility' in titles_html[index:index+300]:
            print(str(i) + ' --> ', titles_html[index:index+100].split('"}]')[0].split('"text":"')[1])
            i = i + 1


#get playlist url from user
pl_url = input("Enter Playlist URL:\n")

#Create Playlist obj
pl = Playlist(pl_url) 

#Num of videos in playlist
video_count = pl.length
remaining_video_count = 0

print(f"Number of videos in the playlist: {video_count}")

print()

print("Videos in the playlist")
print('----------------------------------------------')
index = 0
videos_lst = []
for vid in pl.videos:
    print(str(index) + ' --> ', vid.title)
    index = index + 1
    videos_lst.append(vid)
print('----------------------------------------------')

print()

print("Select videos you want to download...")
print("Ex: 0,2,3,5,6,7 or all")
selection = input("Enter your selection: ")

print('----------------------------------------------')
print()

selected_videos_lst = []
if selection != 'all':
    selection = list(map(int, selection.split(',')))
    selected_videos_lst = [ videos_lst[i] for i in selection ]

elif selection == 'all':
    selected_videos_lst = videos_lst


print("Downloading started...")

for vids in selected_videos_lst:

    vid_url = vids.watch_url
    yt = YouTube(url = vid_url, on_progress_callback=on_progress, on_complete_callback=on_complete) #create Youtube obj

    res_480p = yt.streams.get_by_resolution('480p')
    res_720p = yt.streams.get_by_resolution('720p')
    res_360p = yt.streams.get_by_resolution('360p')

    if(res_720p and yt.streams.filter(file_extension='mp4', progressive=True)): #if the resolution match 480p
        title = yt.title
        print(f"Video title: {title}")
        print("Video download quality: 720p")
        file_size = round((res_720p.filesize / 1000000), 2)
        print(f"File Size: {file_size} MB")
        res_720p.download()
        remaining_video_count += 1
        print("\n")
        
    elif(res_480p and yt.streams.filter(file_extension='mp4', progressive=True)): #if the resolution match 720p
        title = yt.title
        print(f"Video title: {title}")
        print("Video download quality: 480p")
        file_size = round((res_480p.filesize / 1000000), 2)
        print(f"File Size: {file_size} MB")
        res_480p.download()
        remaining_video_count += 1
        print("\n")
        
    elif(res_360p and yt.streams.filter(file_extension='mp4', progressive=True)): #if the resolution match 360p
        title = yt.title
        print(f"Video title: {title}")
        print("Video download quality: 360p")
        file_size = round((res_360p.filesize / 1000000), 2)
        print(f"File Size: {file_size} MB")
        res_360p.download()
        remaining_video_count += 1
        print("\n")

    else:
        print("Low quality video. No video will be downloaded")


    print(f"Downloaded: {remaining_video_count} out of {len(selected_videos_lst)}")

print("Downloading Done...")