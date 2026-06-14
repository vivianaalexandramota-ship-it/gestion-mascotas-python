# Programa tradicional para registrar y mostrar una mascota
# En este archivo NO se utilizan clases ni objetos.


def registrar_mascota():
    """Solicita los datos básicos de una mascota por teclado."""
    print("=== Registro de Mascota ===")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
    """Muestra la información registrada de forma organizada."""
    print("\n=== Información de la Mascota ===")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} años")


def main():
    nombre, especie, edad = registrar_mascota()
    mostrar_mascota(nombre, especie, edad)


if __name__ == "__main__":
    main()
