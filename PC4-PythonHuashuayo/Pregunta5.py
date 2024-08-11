import os

def GuardarTM(n):
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")

def MostrarTM(n):
    nombre_archivo = f"tabla-{n}.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as file:
            print(file.read())
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def MostrarLineaTM(n, m):
    nombre_archivo = f"tabla-{n}.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as file:
            lineas = file.readlines()
            if 1 <= m <= 10:
                print(lineas[m - 1].strip())
            else:
                print("Número m fuera de rango. Debe estar entre 1 y 10.")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        Opcion = input("Seleccione una opción: ")

        if Opcion == '1':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                GuardarTM(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif Opcion == '2':
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                MostrarTM(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif Opcion == '3':
            n = int(input("Ingrese el número n (entre 1 y 10): "))
            m = int(input("Ingrese el número m (entre 1 y 10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                MostrarLineaTM(n, m)
            else:
                print("Los números están fuera del rango, ambos deben estar entre el 1 y el 10")
        
        elif Opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("La opción no es válida, intente nuevamente")

if __name__ == "__main__":
    menu()