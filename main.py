from flask import Flask, render_template
import requests, json

app = Flask(__name__)


def get_meme():
    url = 'https://meme-api.com/gimme'
    response = requests.request(method="GET", url=url).text
    response = json.loads(response)
    meme_pic = response['preview'][-2]
    subreddit = response['subreddit']
    return meme_pic, subreddit

@app.route("/")
def index():
    meme_pic, subreddit =  get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)