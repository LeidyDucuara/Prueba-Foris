from abc import ABC, ABCMeta
from abc import abstractmethod

class IPrensence(metaclass = ABCMeta):
    
    @abstractmethod
    def register_presence(self):
        pass
    
    @abstractmethod
    def all_presences(self):
        pass
    
    @abstractmethod
    def minutes_presence(self):
        pass
    
    