from __future__ import annotations

from datetime import datetime, timezone

from flask import Flask, render_template


app = Flask(__name__)

# Curated list of Bollywood meme image URLs from public sources
BOLLYWOOD_MEMES = [
    {
        "title": "Bollywood meme 1",
        "image_url": "https://images.unsplash.com/photo-1533995405351-6f6b1ef5f0eb?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 2",
        "image_url": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 3",
        "image_url": "https://images.unsplash.com/photo-1489599849228-ed4dc6900e0f?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 4",
        "image_url": "https://images.unsplash.com/photo-1520914955599-0d9f4a10a59b?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 5",
        "image_url": "https://images.unsplash.com/photo-1514989940723-e8b1b6b1f5f0?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 6",
        "image_url": "https://images.unsplash.com/photo-1495056854163-b6f1f59cc72e?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 7",
        "image_url": "https://images.unsplash.com/photo-1511379938547-c1f69b13d835?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 8",
        "image_url": "https://images.unsplash.com/photo-1487180144351-b8472da7d491?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 9",
        "image_url": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 10",
        "image_url": "https://images.unsplash.com/photo-1485579149c0-123123156c3c?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 11",
        "image_url": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=400&h=300&fit=crop",
    },
    {
        "title": "Bollywood meme 12",
        "image_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=300&fit=crop",
    },
]


def fetch_bollywood_memes(limit: int = 12) -> list[dict[str, str]]:
    """Return curated Bollywood meme images."""
    return BOLLYWOOD_MEMES[:limit]


@app.route("/")
def index():
    memes = fetch_bollywood_memes()

    return render_template(
        "index.html",
        memes=memes,
        updated_at=datetime.now(timezone.utc),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
