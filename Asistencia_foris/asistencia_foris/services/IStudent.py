from abc import ABC, ABCMeta
from abc import abstractmethod

class IStudenr(metaclass= ABCMeta):
    
    @abstractmethod
    def register_student(self):
        pass
    
    @abstractmethod 
    def all_students(self):
        pass
    
    @abstractmethod
    def is_student(self):
        pass