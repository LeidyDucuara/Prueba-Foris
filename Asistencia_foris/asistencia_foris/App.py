import argparse
from Ap_asistence import Ap_asistence

class App:
    
    if __name__ == "__main__":
            try:
                # Configurar y obtener parametros
                parser = argparse.ArgumentParser()
                parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
                args = parser.parse_args()

                # Distribuir y ejecutar el proceso seleccionado
                app = Ap_asistence()
                #app.run()
                app.read_file(args)
            except Exception as ex:
                print(f"error generado -->: {ex}")