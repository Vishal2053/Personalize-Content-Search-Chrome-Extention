from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_videos(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 10,  # Get 10 results
        "type": "video"
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    videos = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "url": video_url})

    return videos

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return jsonify([])
    
    return jsonify(get_youtube_videos(query))

if __name__ == "__main__":
    app.run(debug=True)
