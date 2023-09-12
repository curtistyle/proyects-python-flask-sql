# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from msvcrt import getwch

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
#             tracks_items = sp.album_tracks(album['id'])
#             # list_albums.append({'name':album["name"]})
#             print(">>>",album['name'])
#             print()
#             for track in tracks_items["items"]:
#                 getwch()
#                 print(track)
#             print()
        
#     else:
#         print(f"No se encontró el artista '{artist}'.")
        
        
        
# search_albums("The Offspring")       

# from band import Album, Artist, Track

# band = Artist('The Offspring')
# disco = Album('All I Want', 3, 1997)

# pista1 = Track('All I Want', '1::55', 1)
# pista2 = Track('Way Down The Line', '2:37', 2)
# pista3 = Track('Smash It Up', '3:25', 3)

# pista1.Title

# pista1.Artist = band
# pista2.Artist = band
# pista3.Artist = band



# disco.addTrack(pista1)
# disco.addTrack(pista2)
# disco.addTrack(pista3)



# band.Albums = disco

# disco.Track_List[0].Title


# # nuevo_valor = int(input("Ingrese un artista: "))



# try:
#     pista1.Title = 2
# except ValueError as e:
#     print("Error!, ", e)
# print(band)

# print(f"{type('s')} - {type(str())}")


# ! -------------------------------

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

dic_list = []

lista = ['Conspiracy Of One ¯ Want You Bad', 'Conspiracy Of One ¯ Million Miles Away', 'Conspiracy Of One ¯ Dammit, I Changed Again']

def generate_dic(items : list):
    for item in items:
        words = item.split('¯')
        dic_list.append({'artist': words[0],'album': words[1], 'track' : words[2], 'time' : words[3]})

generate_dic(lista)

print(dic_list)
from datetime import datetime



tiempo = 132000 / (1000 * 60)

def convertir_milisegundos_a_minutos_segundos(milisegundos):
    segundos, milisegundos = divmod(milisegundos, 1000)
    minutos, segundos = divmod(segundos, 60)
    return f'{minutos:02}:{segundos:02}'

# Ejemplo de uso
milisegundos = 132000
formato_tiempo = convertir_milisegundos_a_minutos_segundos(milisegundos)
print(formato_tiempo)