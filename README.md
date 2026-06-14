# Sistema de Gestión de Mascotas

**Estudiante:** Geovanny Velasco Paredes

## Descripción del proyecto

Este proyecto contiene dos programas desarrollados en Python para registrar y mostrar información básica de mascotas. Ambos programas trabajan con los mismos datos principales: nombre, especie y edad.

El objetivo es comparar dos formas de programar: la Programación Tradicional y la Programación Orientada a Objetos.

## Estructura del repositorio

```text
Repositorio GitHub
├── programacion_tradicional/
│   └── tradicional.py
├── programacion_poo/
│   ├── main.py
│   └── mascota.py
└── README.md
```

## Programa 1: Programación Tradicional

El programa tradicional se encuentra en la carpeta `programacion_tradicional`.

Archivo principal:

```text
programacion_tradicional/tradicional.py
```

En este programa se utilizan variables y funciones. No se usan clases ni objetos. El usuario ingresa por teclado el nombre, la especie y la edad de la mascota. Luego, el programa muestra la información de manera organizada.

Funciones utilizadas:

- `registrar_mascota()`: solicita los datos mediante teclado.
- `mostrar_mascota()`: presenta los datos ingresados.

## Programa 2: Programación Orientada a Objetos

El programa orientado a objetos se encuentra en la carpeta `programacion_poo`.

Archivos principales:

```text
programacion_poo/main.py
programacion_poo/mascota.py
```

En este programa se utiliza una clase llamada `Mascota`. Esta clase contiene los atributos `nombre`, `especie` y `edad`, además de los métodos `mostrar_informacion()` y `hacer_sonido()`.

En el archivo `main.py` se crean dos objetos de la clase `Mascota` y se ejecutan sus métodos para mostrar la información y el sonido de cada mascota.

## Cómo ejecutar los programas

### Ejecutar el programa tradicional

```bash
cd programacion_tradicional
python tradicional.py
```

### Ejecutar el programa POO

```bash
cd programacion_poo
python main.py
```

## Reflexión personal

Al realizar los dos programas pude notar que la Programación Tradicional es útil para ejercicios pequeños, porque se trabaja de forma directa con funciones y variables. Sin embargo, cuando el programa crece, puede ser más difícil organizar la información.

En cambio, la Programación Orientada a Objetos permite ordenar mejor el código mediante clases y objetos. En este caso, la clase `Mascota` reúne sus datos y acciones en una sola estructura. Esto hace que el programa sea más claro, reutilizable y fácil de modificar.

Por eso, considero que ambos enfoques son importantes, pero la POO ayuda más cuando se necesita desarrollar sistemas con más elementos y mejor organización.
