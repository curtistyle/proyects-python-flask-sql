class Usuario():
    def __init__(self, name) -> None:
        self.name = name
    
    @property
    def Name(self):
        return self.name
    
    @Name.setter
    def Name(self, value):
        self.name = value
    
    def add_user_after(self, value):
        """ add object `User` in list"""
        self.lista_user.append(value)
    
    def __str__(self) -> str:
        return f"{self.name=}, {self.lista_user=}"
    
    def view_list(self) -> str:
        return self.lista_user
    
class Lista():
    def __init__(self, name, user) -> None:
        self.name = name
        self.user = Usuario()
        self.lista_track : list
        
    @property
    def Name(self):
        return self.Name
    
    @property
    def User(self):
        return self.user
    
    @property
    def Lista_Track(self):
        return self.lista_track
    
    @Name.setter
    def Name(self, value):
        self.name = value
        
    @User.setter
    def User(self, value):
        self.user = value
        
    @Lista_Track.setter
    def Lista_Track(self, value):
        self.lista_track = value
        
    def add_track_after(self, value):
        self.lista_track.append(value)
        
    def __str__(self) -> str:
        return f"{self.name=}, {self.user=}, {self.lista_track}"
    
        
class Track():
    def __init__(self, name) -> None:
        self.name = name
        self.artist : Artist() # Artist()
        self.album : Album() # Album()
        self.lista : Lista() # Lista()

    @property
    def Name(self):
        return self.name
    
    @property
    def Artist(self):
        return self.artist
    
    @property
    def Album(self):
        return self.album
    
    @property
    def Lista(self):
        return self.lista
    
    @Name.setter
    def Name(self, value):
        self.name = value
        
    @Artist.setter
    def Artist(self, value):
        self.artist = value
    
    @Album.setter
    def Album(self, value):
        self.album = value
        
    @Lista.setter
    def Lista(self, value):
        self.lista = value
           
    def __str__(self) -> str:
        return f"{self.name=}" 

class Album():
    def __init__(self, name) -> None:
        self.name = name
        self.track : Track() # Track()
        self.artist : Artist() # Artist()
        
    @property
    def Name(self):
        return self.name
    
    @property
    def Track(self):
        return self.track
    
    @property
    def Artist(self):
        return self.artist
    
    @Name.setter
    def Name(self, value):
        self.name = value
    
    @Track.setter
    def Track(self, value):
        self.track = value
        
    @Artist.setter
    def Artist(self, value):
        self.artist = value
    
    def __str__(self) -> str:
        return f"{self.name=}"
    
class Artist():
    def __init__(self, name) -> None:
        self.name = name
        self.album : Album()
        self.track : Track()
    
    @property
    def Name(self):
        return self.name
    
    @property
    def Album(self):
        return self.album
    
    @property
    def Track(self):
        return self.track
    
    @Name.setter
    def Name(self, value):
        self.name = value
        
    @Album.setter
    def Album(self, value):
        self.album = value
        
    @Track.setter
    def Track(self, value):
        self.track = value
        
    def __str__(self) -> str:
        return f"{self.name=}"
        
    
if __name__=="__main__":
    pass