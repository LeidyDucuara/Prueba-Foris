from abc import ABC, ABCMeta
from abc import abstractmethod
import datetime

class IPresence(metaclass = ABCMeta):
    
    '''Registrar una nueva presencia'''
    @abstractmethod
    def register_presence(self, name:str, day:int, start_time: datetime, end_time: datetime, room_code:str):
        pass
    
    '''Retornar todas las presencias registradas'''
    @abstractmethod
    def all_presences(self) -> list:
        pass
    
    '''Retornar la cantidad de minutos que se registro en la presencia'''
    @abstractmethod
    def minutes_presence(self) -> int:
        pass
    