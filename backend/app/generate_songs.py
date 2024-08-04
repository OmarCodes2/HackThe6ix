import requests

def generate_songs_artists(token: str, artist: str):
    songs = []
    
    url = f"https://api.spotify.com/v1/artists/{artist}/top-tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "market": "US"  # Specify the market, you can change it based on your requirement
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for track in data['tracks']:
            songs.append({
                "song_name": track['name'],
                "album_name": track['album']['name'],
                "release_date": track['album']['release_date'],
                "popularity": track['popularity'],
                "preview_url": track['preview_url'],  # This might be None if not available
                "spotify_url": track['external_urls']['spotify']
            })
    else:
        raise Exception(f"Failed to fetch top tracks: {response.status_code}, {response.text}")
    
    return songs