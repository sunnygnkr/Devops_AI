import urllib.request
import json
import os

filenames = [
    "Sachin Tendulkar cropped.jpg",
    "Sachin Tendulkar (2667289620).jpg",
    "Sachin Tendulkar (2667284068).jpg",
    "Sachin Tendulkar waiting.jpg",
    "Sachin Tendulkar 2.jpg",
    "Sachin Tendulkar 1.jpg",
]

save_dir = os.path.join(os.path.dirname(__file__), "static", "images")
headers = {"User-Agent": "SachinGallery/1.0 (educational project)"}


def get_thumb_url(filename):
    encoded = urllib.request.quote(filename)
    api = (
        "https://commons.wikimedia.org/w/api.php"
        "?action=query"
        f"&titles=File:{encoded}"
        "&prop=imageinfo"
        "&iiprop=url"
        "&iiurlwidth=480"
        "&format=json"
    )
    req = urllib.request.Request(api, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    info = page.get("imageinfo")
    if not info:
        raise ValueError("no imageinfo returned")
    return info[0]["thumburl"]


for i, fname in enumerate(filenames, 1):
    dest = os.path.join(save_dir, f"sachin{i}.jpg")
    try:
        url = get_thumb_url(fname)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"[OK]  sachin{i}.jpg  {size//1024}KB")
    except Exception as e:
        print(f"[FAIL] sachin{i}.jpg ({fname}): {e}")
