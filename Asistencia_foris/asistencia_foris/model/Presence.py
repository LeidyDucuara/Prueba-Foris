import datetime

class Presence(object):
    
    presences : dict = {}
    
    def __init__(self, name:str, day:int, start_time: datetime, end_time: datetime, room_code:str):
        self.name = name,
        self.day = day,
        self.start_time = start_time,
        self.end_time = end_time,
        self.room_code = room_code,
        self.presences[name] = {'name' : name,
                                'day': day,
                                'start_time': start_time,
                                'end_time': end_time,
                                'room_code': room_code}
    
    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name:str) -> None:
        self.name = name
        
    @property
    def day(self) -> int:
        return self.day
    
    @day.setter
    def day(self, day:int) -> None:
        self.day = day
        
    @property
    def start_time(self) -> datetime:
        return self.start_time
    
    @start_time.setter
    def start_time(self, start_time:datetime) -> None:
        self.start_time = start_time
        
    @property
    def end_time(self) -> datetime:
        return self.end_time
    
    @end_time.setter
    def end_time(self, end_time:datetime) -> None:
        self.end_time = end_time
        
    @property
    def room_code(self) -> str:
        return self.room_code
    
    @room_code.setter
    def room_code(self, room_code:str) -> None:
        self.room_code = room_code
    