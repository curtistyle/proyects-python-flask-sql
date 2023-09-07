import artist as Artist
import album as Album

class Track():
    
    def __init__(self, title, time, number, artist, album):
        self.__title  : str = title
        self.__time   : str = time
        self.__number : str = number 
        self.__artist : Artist = artist
        self.__album  : Album = album

    def __str__(self) -> str:
        return f"number='{self.__number}' title='{self.__title}' time='{self.__time}'"

    """ Getters """
    @property
    def Title(self):
        return self.__title
    
    @property
    def Time(self):
        return self.__time
    
    @property
    def Number(self):
        return self.__number
    
    @property
    def Artist(self):
        return self.__artist
        
    @property
    def Album(self):
        return self.__album
    
    @Title.setter
    def Title(self,value):
        self.__title = value
    
    @Time.setter
    def Time(self, value):
        self.__time = value

    @Number.setter
    def Number(self, value):
        if (value >= 0):
            self.__number = value
        else:
            assert ValueError("No puede ser negativo.")
            
    @Artist.setter
    def Artist(self, value):
        self.__artist = value
    
    @Album.setter
    def Album(self, value):
        self.__album = value
    
    
