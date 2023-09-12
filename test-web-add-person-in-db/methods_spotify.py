import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de la aplicación
client_id = "aad4ffcc488644c8ac36c765382751be"
client_secret = "dccf369fdec34a9f8de258890cae5b30"

# Inicializar el objeto de autenticación
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

list_albums = []

# def generate_dic(items : list):
#     for item in items:
#     pass
def ms_to_minute(milisegundos):
    segundos, milisegundos = divmod(milisegundos, 1000)
    minutos, segundos = divmod(segundos, 60)
    return f'{minutos:02}:{segundos:02}'

def generate_dic(items : list):
    dic_list = []
    for item in items:
        words = item.split('¯')
        dic_list.append({'artist': words[0],'album': words[1], 'track' : words[2]})
    return dic_list

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
            
            track_list = []
            for track in tracks_items["items"]:
                track_title = track['name']
                track_time = ms_to_minute(track['duration_ms'])
                
                track_list.append({'title':track_title, 'time': track_time})
                   
            list_albums.append({'title': album_title,'year':album_year, 'tracks':track_list,'property':acordion_property,'img':album_img})
            pos += 1
    else:
        print(f"No se encontró el artista '{title_artist}'.")
    #print(list_albums)
    return list_albums
    

    
    

