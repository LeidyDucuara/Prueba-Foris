import datetime
presences : list = []
class Presence(object):
    
    def __init__(self):
        self.__name : str = None,
        self.__day : int = None,
        self.__start_time : datetime = None,
        self.__end_time : datetime = None,
        self.__room_code : str = None
        self.__cant_min : int = None
        
    def save_presence(self, name:str, day:int, start_time: datetime, end_time: datetime, room_code:str, cant_min:int):
        self.__name = name,
        self.__day = day,
        self.__start_time = start_time,
        self.__end_time = end_time,
        self.__room_code = room_code,
        self.__cant_min = cant_min
        presences.append(self)
    
    def all_presences(self) -> list:
        return presences
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        self.__name = name
        
    @property
    def day(self) -> int:
        return self.__day
    
    @day.setter
    def day(self, day:int) -> None:
        self.__day = day
        
    @property
    def start_time(self) -> datetime:
        return self.__start_time
    
    @start_time.setter
    def start_time(self, start_time:datetime) -> None:
        self.__start_time = start_time
        
    @property
    def end_time(self) -> datetime:
        return self.__end_time
    
    @end_time.setter
    def end_time(self, end_time:datetime) -> None:
        self.__end_time = end_time
        
    @property
    def room_code(self) -> str:
        return self.__room_code
    
    @room_code.setter
    def room_code(self, room_code:str) -> None:
        self.__room_code = room_code
        
    @property
    def cant_min(self) -> int:
        return self.__cant_min
    
    @cant_min.setter
    def cant_min(self, cant_min:int) -> None:
        self.__cant_min = cant_min
    