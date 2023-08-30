import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de la aplicación
client_id = "aad4ffcc488644c8ac36c765382751be"
client_secret = "dccf369fdec34a9f8de258890cae5b30"

# Inicializar el objeto de autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


list_albums = []

def search_albums_for_artist(title_artist):
    list_albums = []
    
    pos = 1
    # Buscar el artista
    results = sp.search(q=title_artist, type="artist", limit=1)
    if "artists" in results and "items" in results["artists"]:
        artist_item = results["artists"]["items"][0]
        artist_id = artist_item["id"]
        
        
        
        # Obtener los álbumes del artista
        albums = sp.artist_albums(artist_id, album_type="album")

        for album in albums["items"]:
            acordion_property = "panelsStayOpen-collapse" + str(pos)
            tracks_items = sp.album_tracks(album['id'])
            album_title = album["name"]
            album_year = album['release_date']
            album_img = album['images'][0]['url']
            
            print(">>>")
            track_list = []
            for track in tracks_items["items"]:
                track_list.append(track['name'])
                
            
            #print('>>>',track_list)    
            list_albums.append({'title': album_title,'year':album_year, 'tracks':track_list,'property':acordion_property,'img':album_img})
            pos += 1
    else:
        print(f"No se encontró el artista '{title_artist}'.")
    
    return list_albums
    
    
    

