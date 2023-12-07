from abc import ABC, ABCMeta
from abc import abstractmethod

class IAsistence(metaclass = ABCMeta):
    
    '''Abrir un nuevo registro de asistencia para u estudiante recien inscrito'''
    @abstractmethod
    def register_asistence(self):
        pass
    
    '''Modificar el registro de asistencia si se presenta alguna presencia'''
    @abstractmethod
    def update_asistence(self):
        pass
    
    '''Retornar un resumen con la asistencia de todos los estudiantes'''
    @abstractmethod
    def summary_asistence(self):
        pass
    
    
    