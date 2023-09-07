import artist 
import album 
import track 

# from src.artist import Artist
# from src.album import Album
# from src.track import Track

artista = artist.Artist
disco = album.Album
pista = track.Track


artista.Name = "The Offspring"


disco.Title = "All I Want"
disco.Count = 3
disco.Year = 1997

artista.Albums.append(disco)

pista.Number = 1
pista.Title = "All I Want"
pista.Time = '1:55'
pista.Album = disco

disco.Track_List.append(pista)

pista.Number = 2
pista.Title = "Way Down The Line"
pista.Time = '2:37'
pista.Album = disco

disco.Track_List.append(pista)

pista.Number = 3
pista.Title = "Smash It Up"
pista.Time = '3:25'
pista.Album = disco

disco.Track_List.append(pista)

artista.Albums.apeend(disco)




