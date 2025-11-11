# 🌍 Gestión de Países en Python

## 🧾 Descripción del programa
Este proyecto consiste en una aplicación desarrollada en **Python** que permite **gestionar información sobre países** a partir de un archivo **CSV**.  

El programa aplica estructuras fundamentales como **listas, diccionarios, funciones, condicionales, bucles, ordenamientos y estadísticas básicas**, ofreciendo una interfaz por consola donde el usuario puede consultar, filtrar, ordenar y analizar los datos de forma dinámica.

---

## ⚙️ Instrucciones de uso

### 🔹 1. Requisitos previos
- Tener instalado **Python 3**.
- Contar con el archivo paises.CSV con las columnas: 
Nombre,Poblacion,Superficie,Continente
**Ejemplo:**
Argentina,45000000,2780000,América
España,47000000,505990,Europa
Japón,125800000,377975,Asia

---

### 🔹 2. Ejecución del programa
1. Cloná este repositorio o descargá los archivos `.py` y el `.csv`.
2. Asegurate de que la ruta del CSV sea la misma que la del programa
3. Ejecutá el programa desde la terminal o VSCode:
python TrabajoIntegrador.py

### 🔹 3. Opciones del menú principal
Al iniciar el programa se mostrará el siguiente menú:

GESTIÓN DE PAÍSES

1) Buscar país por nombre
2) Filtrar por continente
3) Filtrar por rango de población
4) Filtrar por rango de superficie
5) Ordenar países
6) Mostrar estadísticas
7) Salir

👉 Ingresá el número de la opción deseada y seguí las instrucciones en pantalla.

## 🧩 Ejemplos de entradas y salidas

### 🔸 Ejemplo 1 – Buscar país

Entrada:

Ingrese nombre o parte del nombre: arg

Salida:

Argelia - Población: 45606480.0 - Superficie: 2381741.0 - Continente: África
Argentina - Población: 45773884.0 - Superficie: 2780400.0 - Continente: América

### 🔸 Ejemplo 2 – Filtrar por continente

Entrada:

Ingrese continente: europa

Salida:

Albania - Población: 2832439.0 - Superficie: 28748.0 - Continente: Europa
Alemania - Población: 84552242.0 - Superficie: 357022.0 - Continente: Europa
Andorra - Población: 79535.0 - Superficie: 468.0 - Continente: Europa

### 🔸 Ejemplo 3 – Mostrar estadísticas

Salida:

País con mayor población: India - 1463865525.0
País con menor población: Vaticano - 825.0
Promedio de población: 41118074
Promedio de superficie: 682639
Cantidad de países por continente:
Asia : 47
Europa : 45
África : 55
América : 35
Oceanía : 14


## 📊 Estructura de datos utilizada

El programa utiliza una lista de diccionarios para almacenar la información de los países.
Cada país se representa como un diccionario con sus atributos, y todos se agrupan dentro de una lista:
paises = [
    {
        "nombre": "Argentina",
        "poblacion": 45000000,
        "superficie": 2780000,
        "continente": "América"
    },
    {
        "nombre": "España",
        "poblacion": 47000000,
        "superficie": 505990,
        "continente": "Europa"
    }
]

Esta estructura facilita la búsqueda, filtrado, ordenamiento y cálculo de estadísticas.

## 🤖 Recursos y aprendizajes aplicados

◼ Lectura y procesamiento de archivos CSV con csv.DictReader.

◼ Manejo de listas y diccionarios en Python.

◼ Creación de funciones modulares y reutilizables.

◼ Uso de estructuras condicionales y bucles.

◼ Implementación de ordenamientos y estadísticas básicas.

◼ Aplicación opcional del módulo unicodedata para mejorar las búsquedas ignorando tildes y mayúsculas.

◼ Uso de inteligencia artificial como apoyo.

### 👨‍💻 Proyecto desarrollado por Joaquín Sánchez