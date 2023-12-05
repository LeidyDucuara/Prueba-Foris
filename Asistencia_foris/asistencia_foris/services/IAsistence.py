from abc import ABC, ABCMeta
from abc import abstractmethod

class IAsistence(metaclass = ABCMeta):
    
    @abstractmethod
    def register_asistence(self):
        pass
    
    @abstractmethod
    def all_asistences(self):
        pass
    
    @abstractmethod
    def add_minutes(self):
        pass
    
    @abstractmethod
    def add_day(self):
        pass
    
    @abstractmethod
    def is_asistence(self):
        pass
    
    
    