import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    FuentesDisponibles = figlet.getFonts()
    FuenteUtilizar = input("Ingrese el nombre de la fuente a utilizar (o presione Enter para seleccionar una aleatoria): ")

    if not FuenteUtilizar:
        FuenteUtilizar = random.choice(FuentesDisponibles)

    if FuenteUtilizar not in FuentesDisponibles:
        print(f"Fuente '{FuenteUtilizar}' no válida, seleccione otra fuente")
        FuenteUtilizar = random.choice(FuentesDisponibles)

    figlet.setFont(font=FuenteUtilizar)

    TextoConvertir = input("Ingrese el texto a convertir: ")
    print(figlet.renderText(TextoConvertir))

if __name__ == "__main__":
    main()