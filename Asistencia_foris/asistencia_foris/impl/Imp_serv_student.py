from services import IStudent
from model.Student import Student
from impl.Impl_serv_asistence import Impl_service_asistence

class Impl_service_student(IStudent.IStudent):
    
    def __init__(self) -> None:
        self.student: Student = Student()

    def all_students(self) -> list:
        """Retorna una lista de los estudiantes guardados

        Returns:
            list: lista con todos los objetos de tipo estudiante
        """        
        students: list = self.student.all_students()
        return students
    
    def register_student(self, name_s :str,asis: Impl_service_asistence):
        """Registra un nuevo estudiante despues de verificar que no exista uno igual y 
        crear su registro de asistencia vacio para que se empiece a actualizar cuando se detecten presencias

        Args:
            name_s (str): nombre del estudiante a registrar
            asis (Impl_service_asistence): Instancia de nuestra clase asistencia
        """        
        try:
            students: list = self.student.all_students()
            flag: bool = True
            if len(students) != 0:
                for student in students:
                    if student.name == name_s:
                        flag = False
                        
            if flag == True:
                self.student: Student = Student()
                self.student.save_student(name_s)
                asis.register_asistence(asis,name_s,0,[],0)
            else:
                print("El estudiante {} ya existe".format(name_s))
        except Exception as ex:
            print(f"error al registrar un studiante -->: {ex}")
    
    
    def is_student(self, name_s:str) -> bool:
        """Valida si existe ya registrado un estuante con el mismo nombre

        Args:
            name_s (str): nombre del estudiante a registrar

        Returns:
            bool: Retrna True si ya existe y False si no
        """        
        try:
            students: list = self.student.all_students()
            flag: bool = False
            if len(students) != 0:
                for student in students:
                    if student.name == name_s:
                        flag = True
                        
            return flag
        except Exception as ex:
                print(f"error al validad si ya existe un estudiante registrado con ese nombre-->: {ex}")

        