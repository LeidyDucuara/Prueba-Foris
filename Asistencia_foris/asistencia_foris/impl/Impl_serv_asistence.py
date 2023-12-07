from services.IAsistence import IAsistence
from model.Asistence import Asistence
import operator

class Impl_service_asistence(IAsistence):
    
    reg_asistence: Asistence = Asistence()
    
    def __init__(self) -> None:
        self.reg_asistence: Asistence = Asistence()
    
    def register_asistence(self, name:str, total_min:int,days: list, cant_days:int):
        """Registrar un nuevo historial de asistencia 

        Args:
            name (str): nombre del estudiante
            total_min (int): total minutos registrados de la presencia
            days (list): los dias que ha registrado presencias
            cant_days (int): cantidad de dias diferentes en los que ha asistido
        """  
        try:      
            self.reg_asistence.save_asistence(name,total_min,days, cant_days)
        except Exception as ex:
                print(f"error al crear un reistro de asistencia-->: {ex}")

    
    def update_asistence(self, name:str, day: int, total_min:int) -> None:
        """Actualiza el registro de asistencias cada que se registra una nueva presencia, 
        se aumenta el total de minutos, si es un dias diferente se añade y se modifica la cantidad de dias 

        Args:
            name (str): nombre del estudiante dueño del registro
            day (int): dia de la semana que se registro la presencia
            total_min (int): los minutos que duro la presencia
        """    
        try:    
            reg: dict = self.reg_asistence.show_asistence(name)
            reg['minutes'] += total_min
            if day not in reg['days']:
                reg['days'].append(day)
            reg['cant_days']= len(reg['days'])
        except Exception as ex:
                print(f"error al actualizar un registro de asistencia -->: {ex}")

        
    def summary_asistence(self) -> list:
        """Generar resumen de asistencia, ordenamos el diccionario y retornamos una lista con los
        valores registrados 

        Returns:
            list: Valores organizados de mayor a menor segun la cantidad de minutos totales
        """      
        try:
            reg: dict = self.reg_asistence.show_asistences()
            resul : list = reg.values()
            res = sorted(resul, key= lambda x:x['minutes'], reverse=True)
            return res
        except Exception as ex:
                print(f"error al ordenar el diccionario original de asistencias -->: {ex}")
