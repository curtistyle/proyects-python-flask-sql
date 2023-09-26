class Track(object):
    def __init__(self, name, artist_name, album_name) -> None:
        self.name = name
        self.artist = Artist(artist_name)
        self.album = Album(album_name)

class Album(object):
    def __init__(self, name) -> None:
        self.name = name
        self.__year : str
        self.track : Track
        self.artist : Artist
    
    @property
    def Year(self):
        """`get` year"""
        return self.__year
    
    @Year.setter
    def Year(self, value):
        """`set` year"""
        self.__year = value
    
class Artist(object):
    def __init__(self, name) -> None:
        self.name = name
        self.album : Album
        self.track : Track

if __name__=="__main__":
    track = Track("Gone Away", "The Offspring", "Smash")
    
    print(track.artist.name)
    
    track.album.Year = "1994"
    
    print(track.album.Year)