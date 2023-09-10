class Track():
    
    def __init__(self, title='', time='', number=0):
        self.__title  : str = title
        self.__time   : str = time
        self.__number : str = number 
        self.__link   : str
        self.__artist : Artist  
        self.__album  : Album 

    def __str__(self) -> str:
        return f"number='{self.__number}' title='{self.__title}' time='{self.__time}'"
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"name={self.__title!r}, "
            f"time={self.__time!r}, "
            f"number={self.__number!r}, ) "
            
        )
        
    def __eq__(self, other):
        if other.__class__ is self.__class__
            return (
                self.__title,
                self.__tme,
                self.__number,
                self.__link,
                self.__artist,
                self.__album
            ) == (
                other.__title,
                other.__time,
                other.__number,
                other.__link,
                other.__artist,
                other.__album
            )
        else:
            return NotImplemented
         
    @property
    def Title(self):
        """Get `Title` atribute from `Track` object."""
        return self.__title
    
    @property
    def Time(self):
        """Get `Title` atribute from `Track` object."""
        return self.__time
    
    @property
    def Number(self):
        """Get `Number` atribute from `Truck` object."""
        return self.__number
    
    @property
    def Artist(self):
        """Get `Artist` atribute from `Track` object."""
        return self.__artist
        
    @property
    def Album(self):
        """Get `Album` atribute from `Track` object."""
        return self.__album
    
    @property
    def Link(self):
        """Get `Link` atribute from `Track` object."""
        return self.__link
    
    @Title.setter
    def Title(self, value):
        if isinstance(value, str):
            self.__title = value
        else:
            raise ValueError("El valor que ingreso debe ser de tipo 'str'.")
        
    @Time.setter
    def Time(self, value):
        self.__time = value

    @Number.setter
    def Number(self, value):
        if (value >= 0):
            self.__number = value
        else:
            raise ValueError("No puede ser negativo.")
            
    @Artist.setter
    def Artist(self, value):
        self.__artist = value
    
    @Album.setter
    def Album(self, value):
        self.__album = value

    @Album.setter
    def Link(self, value):
        self.__link = value
        
        
class Album():
    """ Constructor: se llama cuando se crea una nueva instancia de la clase. """
    def __init__(self, title='', count=0, year=0, img=''):
        self.__title      : str = title
        self.__count      : int = count
        self.__year       : int = year
        self.__img        : str = img
        self.__track_list : list = []
        self.__artist     : Artist
    
    def __eq__(self, other):
        """ Define la igualdad entre dos Objetos. """
        if other.__class__ is  self.__class__: 
            return (
                self.__track_list,
                self.__title,
                self.__count,
                self.__year,
                self.__img,
            ) == (
                other.__track_list,
                other.__title,
                other.__count,
                other.__year,
                other.__img
            )
        else:
            return NotImplemented
    """ Define la desigualdad entro dos Objetos. """ 
    def __ne__(self, other):
        result = self.__eq__(other)
        if result in NotImplemented:
            return NotImplemented
        else:
            return not result
    """ Devuelve una representacion en cadena de caracteres 
    que se utiliza para la representacion oficial del Objeto """
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"title={self.__title!r}, "
            f"count={self.__count!r}, "
            f"year={self.__year!r}, "
            f"img={self.__img!r}, "
            f"track_list={self.__track_list!r} ) "
        )
    
    def __str__(self):
        return f"title={self.__title}, count={self.__count}, year={self.__year}, img={self.__img}"
    
    def __hash__(self):
        return hash((
            self.__class__, 
            self.__track_list, 
            self.__title, 
            self.__count, 
            self.__year, 
            self.__img
        ))
    
    @property
    def Track_List(self):
        return self.__track_list
    
    @property
    def Title(self):
        return self.__title

    @property
    def Count(self):
        return self.__count

    @property
    def Year(self):
        return self.__year
    
    @property
    def Artist(self):
        return self.__artist
    
    @Track_List.setter
    def Track_List(self, value):
        self.__track_list = value
    
    @Title.setter
    def Title(self, value):
        self.__title = value

    @Count.setter
    def Count(self, value):
        if (value >= 0):
            self.__count = value
        else:
            assert ValueError("No puede ser negativo.")
    
    @Year.setter
    def Year(self, value):
        if (value >= 0):
            self.__year = value
        else:
            assert ValueError("No puede ser negativo.") # raise
    
    @Artist.setter
    def Artist(self, value):
        self.__artist = value
    
    """ Methods"""
    def addTrack(self, value):
        self.__track_list.append(value)

class Artist():
    """ Constructor """
    def __init__(self, name=''):
        self.__name : str = name
        self.__albums : list
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"name={self.__name!r}, "
            f"albums={self.__albums!r} ) "
        ) 
   
    """ Get Name atribute from Artist Object """
    @property
    def Name(self):
        return self.__name
    
    """ Get Albums atribute from Artist Object """
    @property
    def Albums(self):
        return self.__albums
    
    """ Set Name atribute in Artist Object """
    @Name.setter
    def Name(self, value):
        self.__name = value
        
    """ Set list Albums objects in Artist Object """
    @Albums.setter
    def Albums(self, value):   
        self.__albums = value
        
    """ set Album object in list Albums """
    def addAlbum(self, value : Album):
        self.__albums.append(value)
    
    
    
