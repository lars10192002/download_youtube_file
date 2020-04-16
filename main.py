from flask import Flask,url_for,redirect
from pytube import YouTube

# pip install pytube3

app = Flask(__name__)


@app.route('/')
def index():
    return 'setup webpage !'

def download_video(URL):
    YouTube(URL).streams.first().download()


URL = 'https://www.youtube.com/watch?time_continue=1&v=Ep3DcTs-L60&feature=emb_logo'
# download_video(URL)


if __name__ == "__main__":
    app.run(port=4040, debug=True)
