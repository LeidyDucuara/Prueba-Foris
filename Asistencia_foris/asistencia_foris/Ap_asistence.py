class Ap_asistence():
    
    data = []
    
    def __init__(self):
        self.data = []
    
    def read_file(self, arg: any):
        with arg.infile as infile:
            datos = infile.readlines()
        print("Contenido del archivo de entrada:")
        print(datos)
        
