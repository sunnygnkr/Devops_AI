from flask import Flask, render_template

app = Flask(__name__)

images = [
    {
        "title": "The Master Blaster",
        "description": "Sachin Tendulkar — World's greatest batsman, 100 international centuries.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Sachin_Tendulkar_in_ICC_World_Twenty20_warm_up_match.jpg/640px-Sachin_Tendulkar_in_ICC_World_Twenty20_warm_up_match.jpg",
    },
    {
        "title": "World Cup 2011 Victory",
        "description": "Sachin lifts the Cricket World Cup at Wankhede Stadium, Mumbai.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sachin_Tendulkar_2012.jpg/640px-Sachin_Tendulkar_2012.jpg",
    },
    {
        "title": "Bharat Ratna Ceremony",
        "description": "Sachin receives the Bharat Ratna — India's highest civilian honour.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Sachin_tendulkar.jpg/640px-Sachin_tendulkar.jpg",
    },
    {
        "title": "Farewell Test — Wankhede 2013",
        "description": "Sachin's emotional farewell speech at his 200th and final Test match.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Sachin_Tendulkar_at_Brabourne_Stadium.jpg/640px-Sachin_Tendulkar_at_Brabourne_Stadium.jpg",
    },
    {
        "title": "Iconic Cover Drive",
        "description": "The cover drive that defined a generation of cricket fans.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Sachin_Tendulkar_playing_a_cover_drive.jpg/640px-Sachin_Tendulkar_playing_a_cover_drive.jpg",
    },
    {
        "title": "Desert Storm — Sharjah 1998",
        "description": "The legendary Sharjah innings against Australia in a sandstorm.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Sachin_Tendulkar_2011.jpg/640px-Sachin_Tendulkar_2011.jpg",
    },
]


@app.route("/")
def index():
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
