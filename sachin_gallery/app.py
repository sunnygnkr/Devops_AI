from flask import Flask, render_template

app = Flask(__name__)

images = [
    {
        "title": "The Master Blaster",
        "description": "Sachin Tendulkar — India's greatest batsman with 100 international centuries.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Sachin_Tendulkar_cropped.jpg/500px-Sachin_Tendulkar_cropped.jpg",
    },
    {
        "title": "The Legend at His Best",
        "description": "A rare close-up of the Little Master during his illustrious career.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Sachin_Tendulkar_%282667289620%29.jpg/500px-Sachin_Tendulkar_%282667289620%29.jpg",
    },
    {
        "title": "Cricket's Greatest Icon",
        "description": "Sachin Tendulkar — the face that defined cricket for a billion fans.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sachin_Tendulkar_%282667284068%29.jpg/500px-Sachin_Tendulkar_%282667284068%29.jpg",
    },
    {
        "title": "The Waiting Champion",
        "description": "Patient, focused, and unmatched — Sachin waiting to bat.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Sachin_Tendulkar_waiting.jpg/500px-Sachin_Tendulkar_waiting.jpg",
    },
    {
        "title": "Tendulkar — A Timeless Portrait",
        "description": "One of cricket's most iconic portraits of the Mumbai maestro.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Sachin_Tendulkar_2.jpg/500px-Sachin_Tendulkar_2.jpg",
    },
    {
        "title": "Sachin Tendulkar — The Icon",
        "description": "24 years of international cricket, 34,000+ runs, and a billion dreams.",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Sachin_Tendulkar_1.jpg/500px-Sachin_Tendulkar_1.jpg",
    },
]


@app.route("/")
def index():
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
