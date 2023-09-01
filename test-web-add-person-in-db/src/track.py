class Track():
    
    def __init__(self):
        self.__title = str()
        self.__time = str()
        self.__number = int()

    def __str__(self) -> str:
        return f"number='{self.__number}' title='{self.__title}' time='{self.__time}'"

    @property
    def Title(self):
        self.__title
    
    @property
    def Time(self):
        self.__time
    
    @property
    def Number(self):
        self.__number
    
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
    
    
