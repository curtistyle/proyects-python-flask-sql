from classes.test.artist import Artist
from classes.test.album import Album
from classes.test.track import Track

class Items():
    def __init__(self) -> None:
        self.register : list
        
        
if __name__=='__main__':
    registro = Items()
    registro.register.append([Artist('Green',30), Album('Dookie', 1994)])
    
