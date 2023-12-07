from abc import ABC, ABCMeta
from abc import abstractmethod

class IStudent(metaclass= ABCMeta):
    
    def __init__(self):
        pass
    '''Registrar un nuevo estudiante '''
    @abstractmethod
    def register_student(self, name : str) -> None:
        pass
    
    '''Retornar todos los estudiantes registrados'''
    @abstractmethod 
    def all_students(self) -> list:
        pass
    
    '''Validar si un estudiante se encuentra registrado'''
    @abstractmethod
    def is_student(self,name:str) -> bool:
        pass