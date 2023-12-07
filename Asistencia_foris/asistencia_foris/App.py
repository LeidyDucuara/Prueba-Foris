import argparse
from Asistence_run import Ap_asistence

class App:
    
    def main():
        # Configurar y obtener parametros
        parser = argparse.ArgumentParser()
        parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
        args = parser.parse_args()

        # Distribuir y ejecutar el proceso seleccionado
        app = Ap_asistence()
        app.run(args)
                
    if __name__ == "__main__":
            try:
                main()
            except Exception as ex:
                print(f"error generado -->: {ex}")