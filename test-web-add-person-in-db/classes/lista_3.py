class Track(object):
    def __init__(self, name) -> None:
        self.name = name
        self.artist = Artist
        self.album = Album

class Album(object):
    def __init__(self, name) -> None:
        self.name = name
        self.__year : str
        self.track : Track
        self.artist : Artist
    

class Artist(object):
    def __init__(self, name) -> None:
        self.name = name
        self.album : Album
        self.track : Track

if __name__=="__main__":
    track = Track('She')
    album = Album('Dookie')
    artist = Artist('Green Day')
    
    track.album = album
    track.artist = artist
    
    album.track = track
    album.artist = artist
    
    artist.album = album
    artist.track = track
    
    print(album.track.album.name)
    
    





    # @property
    # def Year(self):
    #     """`get` year"""
    #     return self.__year
    
    # @Year.setter
    # def Year(self, value):
    #     """`set` year"""
    #     self.__year = value
    