import track as Track
import artist as Artist

class Album():
    """ Constructor: se llama cuando se crea una nueva instancia de la clase. """
    def __init__(self, track_list, title, count, year, img, artist):
        self.__track_list : list(Track) = track_list
        self.__title      : str() = title
        self.__count      : int() = count
        self.__year       : int() = year
        self.__img        : str() = img
        self.__artist     : Artist = artist
    """ Define la igualdad entre dos Objetos. """
    def __eq__(self, other):
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
            f"track_list={self.__track_list!r}, "
            f"title={self.__title!r}, "
            f"count={self.__count!r}, "
            f"year={self.__year!r}, "
            f"img={self.__img!r} ) "
        )
    
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
    