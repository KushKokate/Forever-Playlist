import spotipy
import requests
import pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# TAKING THE INPUT FOR THE YEAR
date = input("Which year do you want to travel to? Type the Date in this format YYYY-MM-DD: ")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",  # Updated scope to include playlist-modify-public
        redirect_uri="http://localhost:8888/callback",
        client_id="id will go here",
        client_secret="client will go here",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR_USERNAME",
    )
)
user_id = sp.current_user()["id"]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
pprint.pp(song_names)

def playlist_creation():
    user = user_id
    playlist_name = date
    public_playlist = True
    collaborative_playlist = True
    playlist_description = f"These were the top songs on {date}"
    playlist = sp.user_playlist_create(user=user_id,
                                       name=playlist_name,
                                       public=public_playlist,
                                       collaborative=collaborative_playlist,
                                       description=playlist_description)
    playlist_id = playlist['id']  # Get the playlist ID from the created playlist

    # Add songs to the playlist using the track URIs
    track_uris = []  # Initialize an empty list to store track URIs
    for song_name in song_names:
        results = sp.search(q=song_name, limit=1)  # Search for the song on Spotify
        if results['tracks']['items']:  # If search results are found
            track_uris.append(results['tracks']['items'][0]['uri'])  # Add the track URI to the list

    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_uris)  # Add tracks to the playlist

    print(f"Playlist created successfully. Playlist ID: {playlist_id}")

playlist_creation()
