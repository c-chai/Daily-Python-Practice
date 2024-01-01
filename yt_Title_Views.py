# Create a program which shows you the title and number of views of any YouTube link

from pytube import YouTube

def get_youtube_video_info(url):
    try:
        yt = YouTube(url)
        title = yt.title
        views = yt.views
        return title, views
    except Exception as e:
        print("An error occurred:", e)
        return None, None

# Example Usage
url = input("Enter the URL of the YouTube video: ")
title, views = get_youtube_video_info(url)

if title is not None:
    print(f"Title: {title}")
    print(f"Views: {views}")
else:
    print("Failed to retrieve video information.")
