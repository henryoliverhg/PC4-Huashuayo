def ContarLineas(RutaArchivo):
    try:
        if not RutaArchivo.endswith(".py"):
            print("El archivo no es un archivo .py válido")
            return
        
        with open(RutaArchivo, 'r') as file:
            lineas = file.readlines()
        
        lineas_codigo = 0
        
        for linea in lineas:
            linea = linea.strip()
            # Ignorar líneas en blanco o líneas que son solo comentarios
            if linea and not linea.startswith("#"):
                lineas_codigo += 1
        
        print(f"El archivo '{RutaArchivo}' tiene {lineas_codigo} líneas de código")
    
    except FileNotFoundError:
        print(f"El archivo '{RutaArchivo}' no existe")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Contar líneas de código en un archivo .py")
        print("2. Salir")
        Opcion = input("Seleccione una opción: ")

        if Opcion == '1':
            RutaArchivo = input("Ingrese la ruta y nombre del archivo .py: ")
            ContarLineas(RutaArchivo)
        
        elif Opcion == '2':
            print("Saliendo del programa...")
            break
        
        else:
            print("La opción no es válida, intente nuevamente")

if __name__ == "__main__":
    menu()