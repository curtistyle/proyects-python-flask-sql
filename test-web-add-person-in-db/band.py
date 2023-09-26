import flask

class Artist():
    """ Constructor """
    def __init__(self, name=''):
        self.__name : str = name
        self.__album_list = []
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"name={self.__name!r}, "
            f"albums={self.__albums!r} ) "
        ) 
   
    """ Get Name atribute from Artist Object """
    @property
    def name(self):
        return self.__name
    
    """ Get Albums atribute from Artist Object """
    @property
    def album_list(self):
        return self.__album_list
    
    """ Set Name atribute in Artist Object """
    @name.setter
    def name(self, value):
        self.__name = value
        
    """ Set list Albums objects in Artist Object """
    @album_list.setter
    def album_list(self, value):   
        self.__album_list = value
        
    """ set Album object in list Albums """
    def addAlbum(self, value):
        self.__album_list.append(value)
    

class Album():
    """ Constructor: se llama cuando se crea una nueva instancia de la clase. """
    def __init__(self, title='', count=0, year=0, img=''):
        self.__title      : str = title
        self.__count      : int = count
        self.__year       : int = year
        self.__img        : str = img
        self.__track_list : list = []
        
    
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
    def __ne__(self, other):
        """ Define la desigualdad entro dos Objetos. """ 
        result = self.__eq__(other)
        if result in NotImplemented:
            return NotImplemented
        else:
            return not result
    def __repr__(self):
        """ Devuelve una representacion en cadena de caracteres que se utiliza para la representacion oficial del Objeto """
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
    def track_list(self):
        return self.__track_list
    
    @property
    def title(self):
        return self.__title

    @property
    def count(self):
        return self.__count

    @property
    def year(self):
        return self.__year
    
    @track_list.setter
    def track_list(self, value):
        self.__track_list = value
    
    @title.setter
    def title(self, value):
        self.__title = value

    @count.setter
    def count(self, value):
        if (value >= 0):
            self.__count = value
        else:
            assert ValueError("No puede ser negativo.")
    
    @year.setter
    def year(self, value):
        if (value >= 0):
            self.__year = value
        else:
            assert ValueError("No puede ser negativo.") # raise
    
    """ Methods"""
    def addTrack(self, value):
        self.__track_list.append(value)

class Track():
    def __init__(self, title='', number=0):
        self.__title  : str = title
        self.__number : str = number 
        self.__time   : str 
        self.__link   : str 

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
        if other.__class__ is self.__class__:
            return (
                self.__title,
                self.__tme,
                self.__number,
                self.__link
            ) == (
                other.__title,
                other.__time,
                other.__number,
                other.__link
            )
        else:
            return NotImplemented
         
    @property
    def title(self):
        """Get `Title` atribute from `Track` object."""
        return self.__title
    
    @property
    def time(self):
        """Get `Title` atribute from `Track` object."""
        return self.__time
    
    @property
    def number(self):
        """Get `Number` atribute from `Truck` object."""
        return self.__number
    
    @property
    def link(self):
        """Get `Link` atribute from `Track` object."""
        return self.__link
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value
        else:
            raise ValueError("El valor que ingreso debe ser de tipo 'str'.")
        
    @time.setter
    def time(self, value):
        self.__time = value

    @number.setter
    def number(self, value):
        if (value >= 0):
            self.__number = value
        else:
            raise ValueError("No puede ser negativo.")

    @link.setter
    def link(self, value):
        self.__link = value
    
    def get_time_formatted(self):
        pass
        
        

if __name__=="__main__":
    track = Track("She", 8)
    
    print(track.time)
    
    
