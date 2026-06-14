# Clase Mascota
# Este archivo evidencia el uso de clase, atributos y métodos.


class Mascota:
    """Representa una mascota con nombre, especie y edad."""

    def __init__(self, nombre, especie, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Muestra la información principal de la mascota."""
        print("=== Información de la Mascota ===")
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    def hacer_sonido(self):
        """Muestra un sonido general según la especie de la mascota."""
        especie = self.especie.lower()

        if especie == "perro":
            print(f"{self.nombre} hace: ¡Guau guau!")
        elif especie == "gato":
            print(f"{self.nombre} hace: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido propio de su especie.")
