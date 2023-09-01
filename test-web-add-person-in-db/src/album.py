from track import *

class Album():

    def __init__(self):
        self.__track_list = list(Track())
        self.__title = str()
        self.__count = int()
        self.__year = int()
        self.__img = str()

    @property
    def Track_List(self):
        self.__track_list
    
    @property
    def Title(self):
        self.__title

    @property
    def Count(self):
        self.__count

    @property
    def Year(self):
        self.__year
    
    @Track_List.setter
    def Track_List(self, value):
        self.__track_list = value
    
    @Title.setter
    def Title(self, value):
        self.__title = value

    @Count.setter
    def Count(self, value):
        if value >= 0:
            self.__count = value
        else:
            assert ValueError("")
    