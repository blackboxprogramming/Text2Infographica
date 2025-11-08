import requests

def get_youtube_videos(query, max_results=5, api_key="YOUR_YOUTUBE_API_KEY"):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        "part": "snippet",
        "q": query,
        "key": api_key,
        "maxResults": max_results,
        "type": "video"
    }

    response = requests.get(search_url, params=params)
    data = response.json()
    results = []

    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            thumbnail = item["snippet"]["thumbnails"]["medium"]["url"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            results.append({
                "title": title,
                "thumbnail": thumbnail,
                "link": video_url
            })
    
    return results
