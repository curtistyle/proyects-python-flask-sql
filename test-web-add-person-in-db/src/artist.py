import album as Album


class Artist():
    """ Constructor """
    def __init__(self, name, album):
        self.__name : str = name
        self.__albums : list(Album) = album 
        
    
    """ Getters """
    @property
    def Name(self):
        return self.__name
    
    @property
    def Albums(self):
        return self.__albums
    
    """ Setter """
    @Name.setter
    def Name(self, value):
        self.__name = value
        
    @Albums.setter
    def Albums(self, value):
        self.__albums = value
        
    