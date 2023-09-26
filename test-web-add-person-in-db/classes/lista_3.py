class Artist(object):
    def __init__(self, title, amount) -> None:
        self.title = title
        self.amount = amount
        
        self.list_album = []
        
    def add_album(self, value):
        self.list_album.append(value)
        
class Album(object):
    def __init__(self, title, year, amount) -> None:
        self.title = title
        self.year = year
        self.amount = amount
        
        self.list_track = []
        
    def add_track(self, value):
        self.list_track.append(value)
    
class Track(object):
    def __init__(self, title, time) -> None:
        self.title = title
        self.time = time
        



if __name__=="__main__":
    lista = []
    
    track = Track('She', '04:12')
    
    album = Album('Dookie', '1994', 14)
    
    album.add_track(track)
    
    artist = Artist('Green Day', 25)
    
    artist.add_album(album)
    

    print(artist.list_album[0].title)





















    # lista = []
    
    # artist = Artist('Green Day')
    
    # lista.append(artist)
    
    # album = Album('Dookie', artist)
    
    # track = Track('She', album, artist)
    
    
    # print(artist.track.name)
    
    
    
    
    
    
    
    
    

















    # track = Track('She')
    # album = Album('Dookie')
    # artist = Artist('Green Day')
    
    # track.album = album
    # track.artist = artist
    
    # album.track = track
    # album.artist = artist
    
    # artist.album = album
    # artist.track = track
    
    
    
    





    # @property
    # def Year(self):
    #     """`get` year"""
    #     return self.__year
    
    # @Year.setter
    # def Year(self, value):
    #     """`set` year"""
    #     self.__year = value
    