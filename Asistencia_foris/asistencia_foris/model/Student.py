estudents : list = []
class Student(object):
    
    def __init__(self) -> None:
        self.__name :str = None
    
    def save_student(self, name: str) -> None:
        self.__name = name
        estudents.append(self)
    
    def show_student(self):
        print("Nombre: {}".format(self.__name))
        
    def all_students(self) -> list:
        return estudents
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        self.__name = name