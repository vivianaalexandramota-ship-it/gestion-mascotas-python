# Programa orientado a objetos para registrar y mostrar mascotas
# Se utiliza la clase Mascota, objetos, atributos y métodos.

from mascota import Mascota


def main():
    print("=== Sistema de Gestión de Mascotas - POO ===\n")

    # Creación de objetos de la clase Mascota
    mascota1 = Mascota("Firulais", "Perro", 3)
    mascota2 = Mascota("Michi", "Gato", 2)

    # Uso de métodos de cada objeto
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    print()

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()


if __name__ == "__main__":
    main()
