from impl.Imp_serv_student import Impl_service_student
from impl.Impl_serv_presence import Impl_service_presence
from impl.Impl_serv_asistence import Impl_service_asistence

class Ap_asistence():
    
    def run(self,args: any): 
        """ Función principal para ejecutar la logica del problema, vamos a leer el archivo, registrar
        los datos y mostrar un resumen sobre la asistencia de los estudiante en orden desendente. 
        Args:
            args (any): Argumento de tipo archivo recibido por consola
        Returns:
            out_file : archivo con un reporte que liste cada estudiante con el total de minutos 
            registrados y la cantidad de días que asistió a la universidad.
        """   
        stu: Impl_service_student = Impl_service_student()
        pre: Impl_service_presence = Impl_service_presence()
        asis: Impl_service_asistence = Impl_service_asistence
            
        def read_file(arg: any) -> list:     
            """ Función para leer el archivo
            Args:
                arg (any): archivo txt 
            Returns:
                data (list): Lista con las lineas contenidas en el archivo
            """
            try:
                with arg.infile as infile:
                    data : list = infile.readlines()
                return data
            except Exception as ex:
                print(f"error al leer el archivo -->: {ex}")

            
        def register_data(datos: list) -> None:
            """ Función para registrar los datos leidos
            Args:
                datos (list): Lista con los datos a registrar
            """
            try:
                for line in datos:
                    data_line : list = line.replace('\n','').split(' ')
                    command, name,*_ = data_line
                    if command == 'Student':
                        stu.register_student(name,asis)
                    elif command == 'Presence':
                        command, name, day, start, end, room = data_line
                        if stu.is_student(name):
                            pre.register_presence(name, day, start, end, room,asis)
                        else: 
                            print('El estudiante no ha sido registrado')
                    else:
                        print('Opción no soportada')
            except Exception as ex:
                print(f"error al registrar los datos -->: {ex}")

                
        def report_asistence():
            """Esta funcion crea un reporte sobre la asistencia de los estudiantes organizandolos de 
            mayor a menor segun sus minutos de asistencia
            """     
            try:       
                asistences: list = asis.summary_asistence(asis)
                mensaje : str = """{name} : {minutes} minutos in {cant_days} days"""
                for a in asistences:
                    resul = mensaje.format(**a)
                    print(resul)
            except Exception as ex:
                print(f"error al generar el reporte -->: {ex}")

                
        try:
            data = read_file(args)
            register_data(data)
            report_asistence()
            
        except Exception as ex:
                print(f"error al ejecutar la clase ap_asistence -->: {ex}")
