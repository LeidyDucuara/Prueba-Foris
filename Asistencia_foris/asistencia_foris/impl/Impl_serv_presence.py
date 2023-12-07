from datetime import datetime
from services import IPresence
from model.Presence import Presence
from impl.Impl_serv_asistence import Impl_service_asistence

class Impl_service_presence(IPresence.IPresence):
    
    def __init__(self) -> None:
        self.presence: Presence = Presence()
    
    def cant_min(self, start_time:str, end_time:str ) -> int:
        """Recibe dos formatos de hora y retorna la cantidad de minutos entre ellas_

        Args:
            start_time (str): Hora inicial formato (HH:MM)
            end_time (str): Hora final formato (HH:MM)

        Returns:
            int: cantidad de minutos registrados entre horas
        """   
        try: 
            start_presence = datetime.strptime(start_time, "%H:%M")
            end_presence = datetime.strptime(end_time, "%H:%M")
            time_interval = end_presence - start_presence
            tsec:int = time_interval.total_seconds()
            tmin:int = tsec / 60
            return tmin
        except Exception as ex:
                print(f"error al calcular la cantidad de minutos entre horas -->: {ex}")

    
    def register_presence(self, name:str, day:int, start_time: str, end_time: str, room_code:str, asis: Impl_service_asistence):
        """Registra una nueva presencia, valida la cantidad de minutos, si es menor a 5 se descarta el registro
        y tambien verifica que el numero de dia este en un intervalo admitido

        Args:
            name (str): nombre del estudiante
            day (int): dia de la semana [1-7]
            start_time (str): hora inicio formato (HH:MM)
            end_time (str): hora final formate (HH:MM)
            room_code (str): codigo de sala donde se detecto la presencia
            asis (Impl_service_asistence): instancia de asistencia
        """        
        try:
            min_presence = self.cant_min(start_time, end_time)
            if min_presence > 5:
                if int(day) >= 1 and int(day) <= 7:
                    self.precense: Presence = Presence()
                    self.precense.save_presence(name, day, start_time, end_time, room_code, min_presence)
                    asis.update_asistence(asis,name, day, min_presence)
                else:
                    print('El día debe estar entre 1 y 7')    
            else:
                print('El tiempo de presencia debe ser mayor a 5 minutos')
        except Exception as ex:
            print(f"error al registrar una presencia -->: {ex}")

    def all_presences(self) -> list:
        """Retorna una lista con todas las presencias registradas

        Returns:
            list: lista con registros de tipo presence
        """        
        presences :list = self.presence.all_presences()
        return presences
    
    def minutes_presence(self) -> int:
        """Retorna la cantidad de minutos que duro una presencia en particulas

        Returns:
            int: cantidad de minutos
        """        
        return self.precense.cant_min