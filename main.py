from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from pytube import YouTube


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

def download_video(URL):
    YouTube(URL).streams.first().download()


URL = 'https://www.youtube.com/watch?time_continue=1&v=Ep3DcTs-L60&feature=emb_logo'
# download_video(URL)


if __name__ == "__main__":
    app.run(port=4040, debug=True)
