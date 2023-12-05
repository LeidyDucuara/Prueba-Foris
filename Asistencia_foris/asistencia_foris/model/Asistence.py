class Asistence:
    
    asistences : dict = {}
    
    def __init__(self, name:str, total_min:int, cant_days:int):
        self.name = name
        self.total_min = total_min
        self.cant_days = cant_days
        self.asistences[name] = {'name': name,
                                 'total_min': total_min,
                                 'cant_days': cant_days}
        
    @property
    def name(self) -> str:
        return self.name
    
    @name.setter
    def name(self, name : str) -> None:
        self.name = name
        
    @property
    def total_min(self) -> int:
        return self.total_min
    
    @total_min.setter
    def total_min(self, total_min: int) -> None:
        self.total_min = total_min
        
    @property
    def cant_days(self) -> int:
        return self.cant_days
    
    @cant_days.setter
    def cant_days(self, cant_days: int) -> None:
        self.cant_days = cant_days