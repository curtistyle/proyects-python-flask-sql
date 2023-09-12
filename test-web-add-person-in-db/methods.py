import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from band import Album, Track, Artist

class SpotifyMethods():

    def __init__(self):
        self.__client_id = "aad4ffcc488644c8ac36c765382751be"
        self.__client_secret = "dccf369fdec34a9f8de258890cae5b30"
        
    def initialize(self):
        """Initialize the authentication object"""
        auth_manager = SpotifyClientCredentials(client_id=self.__client_id, client_secret=self.__client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp
        

    def get_artist(self,title_artist : str):
        """return albums"""
        
        
        
        list_albums = []
        
        sp = self.initialize()
        
        pos = 1
        # Buscar el artista
        results = sp.search(q=title_artist, type="artist", limit=1)
        artist = Artist()
        if "artists" in results and "items" in results["artists"]:
            artist_item = results["artists"]["items"][0]
            artist_id = artist_item["id"]
            artist.Name = title_artist
            
            
            # Obtener los álbumes del artista
            albums = sp.artist_albums(artist_id, album_type="album")
            
            for ialbum in albums["items"]:
                album = Album()
                acordion_property = "panelsStayOpen-collapse" + str(pos)
                tracks_items = sp.album_tracks(ialbum['id'])
                album.Title= ialbum["name"]
                #album.Year = ialbum['release_date']
                ASD= ialbum['images'][0]['url']
                
                
                
                track_list = []
                # for track in tracks_items["items"]:
                #     track_list.append(track['name'])
                    
                
                for item in tracks_items["items"]:
                    track = Track()
                    track.Title= item["name"]
                    track.Time= item["duration_ms"]
                    track.Number=item["track_number"]
                    album.addTrack(track)
                
                
                artist.addAlbum(album)
                #print('>>>',track_list)    
                #list_albums.append({'title': album_title,'year':album_year, 'tracks':track_list,'property':acordion_property,'img':album_img})
                pos += 1
        else:
            print(f"No se encontró el artista '{title_artist}'.")
        #print(list_albums)
        print(artist.Albums[0].Track.Title)
        return list_albums


if __name__ == '__main__':
    mandale = SpotifyMethods()
    mandale.initialize()
    mandale.get_artist("The Offspring")