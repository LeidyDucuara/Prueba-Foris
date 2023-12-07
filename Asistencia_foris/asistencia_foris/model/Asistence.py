class Asistence(object):
    
    asistence:dict = {}
    
    def __init__(self):
        self.asistence = {}
        
    def save_asistence(self,name:str, total_min:int,days: list, cant_days:int)-> None:
        self.asistence[name] = {'name' : name, 'minutes' : total_min, 'days' : days, 'cant_days' : cant_days}
        
    def show_asistences(self) -> dict:
        return self.asistence
    
    def show_asistence(self,name :str) -> dict:
        return self.asistence[name]
    
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