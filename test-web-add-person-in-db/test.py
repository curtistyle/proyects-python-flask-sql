# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# # Credenciales de la aplicación
# client_id = "aad4ffcc488644c8ac36c765382751be"
# client_secret = "dccf369fdec34a9f8de258890cae5b30"

# # Inicializar el objeto de autenticación
# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(auth_manager=auth_manager)


# list_albums = []

# def search_albums(artist):
#     # Buscar el artista
#     results = sp.search(q=artist, type="artist", limit=1)
#     if "artists" in results and "items" in results["artists"]:
#         artist = results["artists"]["items"][0]
#         artist_id = artist["id"]
        
#         # Obtener los álbumes del artista
#         albums = sp.artist_albums(artist_id, album_type="album")

#         for album in albums["items"]:
#             list_albums.append({'name':album["name"]})
            
#         print(list_albums)
#     else:
#         print(f"No se encontró el artista '{artist}'.")
        

from band import Album, Artist, Track

band = Artist('The Offspring')
disco = Album('All I Want', 3, 1997)

pista1 = Track('All I Want', '1::55', 1)
pista2 = Track('Way Down The Line', '2:37', 2)
pista3 = Track('Smash It Up', '3:25', 3)

pista1.Title

pista1.Artist = band
pista2.Artist = band
pista3.Artist = band



disco.addTrack(pista1)
disco.addTrack(pista2)
disco.addTrack(pista3)



band.Albums = disco

disco.Track_List[0].Title


# nuevo_valor = int(input("Ingrese un artista: "))



try:
    pista1.Title = 2
except ValueError as e:
    print("Error!, ", e)
print(band)

print(f"{type('s')} - {type(str())}")

# from src.artist import Artist
# from src.album import Album
# from src.track import Track

# artista = artist.Artist
# disco = album.Album
# pista = track.Track


# artista.Name = "The Offspring"


# disco.Title = "All I Want"
# disco.Count = 3
# disco.Year = 1997

# artista.Albums = disco

# print(artista.Albums)

# pista.Number = 1
# pista.Title = "All I Want"
# pista.Time = '1:55'
# pista.Album = disco

# disco.Track_List.append(pista)

# pista.Number = 2
# pista.Title = "Way Down The Line"
# pista.Time = '2:37'
# pista.Album = disco

# disco.Track_List.append(pista)

# pista.Number = 3
# pista.Title = "Smash It Up"
# pista.Time = '3:25'
# pista.Album = disco

# disco.Track_List.append(pista)




