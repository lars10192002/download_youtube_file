from pytube import YouTube
# pip install pytube3

URL = 'https://www.youtube.com/watch?v=NyBSv5A5IYA&list=PLkDDOXUP5D2jXIWfqrgRrLLSjDYX-KDDL&index=2&t=0s'
YouTube(URL).streams.first().download()

