from spotipy import Spotify, SpotifyClientCredentials
from band import Album, Artist, Track
import json 

class File():
    def __init__(self, name) -> None:
        self.__path = self.name + ".json"
        self.name = name
        self.__file 
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, value):
        self.__path = value;

    def create(self):
        self.__file = open(self.__path, "w")
        self.__file.close()    
    
        
    def add(self, name_list, **kwargs):
        
        
    

    @staticmethod
    def generate_list(items : list, list_select):
        """Retorna una `lista` con los items formateados. Donde `item` contiene `artista`, `album`, `track`. `list_select` la lista seleccionada que hace referencia al item."""
        list_items = list()
        for item in items:
            words = item.split('¯')
            list_items.append({'artist': words[0], 'album': words[1], 'track' : words[2], 'list_select' : list_select})
        return list_items  
    
    

class Spotify():
    # credenciales de la aplicacion
    __client_id = "aad4ffcc488644c8ac36c765382751be"
    __client_secret = "dccf369fdec34a9f8de258890cae5b30"
    
    __auth_manager = SpotifyClientCredentials(client_id=__client_id, client_secret=__client_secret)
    
    def __init__(self) -> None:
        self.__sp = Spotify(auth_manager=Spotify.__auth_manager)
    
    def search(self,name):
            
            # Buscar el artista
            results = self.__sp.search(q=name, type="artist", limit=1)
            
            if "artists" in results and "items" in results["artists"]:
                
                artist_item = results["artists"]["items"][0]
                artist_id = artist_item["id"]
                
                # * Artist()
                artist = Artist(artist_item["name"])
                
                # Lista de Album()
                list_albums = []
                pos = 1
                
                # Obtener los álbumes del artista
                sp_albums = self.__sp.artist_albums(artist_id, album_type="album")

                for sp_album in sp_albums["items"]:
                    
                    acordion_property = "panelsStayOpen-collapse" + str(pos)
                    
                    # * Album()
                    album = Album(sp_album["name"], sp_album["total_tracks"], sp_album['release_date'], sp_album['images'][0]['url'])
                    
                    sp_tracks = self.__sp.album_tracks(album['id'])
                    
                    # Lista de Track()
                    track_list = []
                    
                    for sp_track in sp_tracks["items"]:
                        
                        # * Track()
                        track = Track(sp_track['name'], sp_track["track_number"], sp_track['duration_ms'])                        
                        
                        track_list.append({'title':track.title, 'time': track.time})
                        
                    list_albums.append({'title': album.title,'year':album.year, 'tracks':track_list,'property':acordion_property,'img':album.img})
                    pos += 1
            else:
                print(f"No se encontró el artista '{name}'.")
            # ! garbage collector
            del artist, album, track
            return list_albums
    