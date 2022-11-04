import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import json
from selenium import webdriver


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_client_id",
                                                           client_secret="your_client_secret",
                                                           redirect_uri= "http://example.com",
                                                           scope="streaming"))


oauth_object = spotipy.SpotifyOAuth("your_client_id","your_client_secret","http://example.com")
token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']

sp = spotipy.Spotify(auth=token)

user = sp.current_user()

# print(json.dumps(user,sort_keys=True, indent=4))

espacement = "-" * 30

while True:
    print("Bienvenue, "+ user['display_name'])
    print("0 - Quitter")
    print("1 - Rechercher une musique")
    print(espacement)
    choice = int(input("Ton choix: "))
    if choice == 1:
        # Get the Song Name.
        searchQuery = input("Entrer le nom de la chanson: ")
        print(espacement)
        # Search for the Song.
        searchResults = sp.search(searchQuery, limit = 10, offset = 0, type = "track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        for i in range(len(tracks_items)):
            if searchQuery in tracks_items[i]['name']:
                print(f"{i} - {tracks_items[i]['name']} - {tracks_items[i]['album']['artists'][0]['name']}")
        print(" " * 30)
        track_wanted = int(input("Laquelle vous souhaitez ? Indiquez le numero: "))
        song = tracks_items[track_wanted]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('La chanson est lancee !.')
        print(espacement)
    elif choice == 0:
        break
    else:
        print("Veuillez entrer un choix valide")
    

