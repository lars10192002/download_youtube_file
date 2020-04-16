from pytube import YouTube
# pip install pytube3


def download_video(URL):
    YouTube(URL).streams.first().download()


URL = 'https://www.youtube.com/watch?time_continue=1&v=Ep3DcTs-L60&feature=emb_logo'
download_video(URL)