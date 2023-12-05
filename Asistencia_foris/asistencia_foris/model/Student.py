class Student:
    
    students : list = []
    
    def __init__(self, name: str):
        self.name : str = name
        self.students.append(name)
        
    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name:str) -> None:
        self.name = name