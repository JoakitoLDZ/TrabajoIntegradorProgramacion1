import csv
import os
import unicodedata  # para eliminar tildes

# --- Función auxiliar para quitar tildes y comparar texto ---
def normalizar_texto(texto):
    """Convierte el texto a minúsculas y elimina tildes."""
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Carga los datos desde un archivo CSV y los guarda en una lista de diccionarios
def cargar_csv(ruta):
    paises = []
    archivo = open(ruta, "r", encoding="utf-8")
    lector = csv.DictReader(archivo)  # Lee el CSV con los encabezados como claves
    for fila in lector:
        d = {}
        d["nombre"] = fila["Nombre"]
        d["poblacion"] = float(fila["Poblacion"])   # Convierte a número decimal
        d["superficie"] = float(fila["Superficie"]) # Convierte a número decimal
        d["continente"] = fila["Continente"]
        paises.append(d)
    archivo.close()
    return paises

# Muestra en pantalla los datos de un país
def mostrar_pais(p):
    print(p["nombre"], "- Población:", p["poblacion"], "- Superficie:", p["superficie"], "- Continente:", p["continente"])

# Busca países por nombre o parte del nombre
def buscar_pais(paises):
    nombre = input("Ingrese nombre o parte del nombre: ").strip()
    nombre = normalizar_texto(nombre)  # Se normaliza para ignorar tildes y mayúsculas
    encontrados = []
    for p in paises:
        if nombre in normalizar_texto(p["nombre"]):
            encontrados.append(p)
    if len(encontrados) == 0:
        print("No se encontraron países con ese nombre.")
    else:
        for p in encontrados:
            mostrar_pais(p)

# Filtra los países según el continente ingresado
def filtrar_por_continente(paises):
    cont = input("Ingrese continente: ").strip()
    cont = normalizar_texto(cont)  # Se normaliza
    filtrados = []
    for p in paises:
        if normalizar_texto(p["continente"]) == cont:
            filtrados.append(p)
    if len(filtrados) == 0:
        print("No hay países en ese continente.")
    else:
        for p in filtrados:
            mostrar_pais(p)

# Filtra los países dentro de un rango de población
def filtrar_por_poblacion(paises):
    minimo = input("Ingrese población mínima: ")
    maximo = input("Ingrese población máxima: ")
    if not minimo.isdigit() or not maximo.isdigit():  # Verifica que sean números
        print("Valores inválidos.")
        return
    minimo = int(minimo)
    maximo = int(maximo)
    filtrados = []
    for p in paises:
        if p["poblacion"] >= minimo and p["poblacion"] <= maximo:
            filtrados.append(p)
    if len(filtrados) == 0:
        print("No hay países en ese rango de población.")
    else:
        for p in filtrados:
            mostrar_pais(p)

# Filtra los países dentro de un rango de superficie
def filtrar_por_superficie(paises):
    minimo = input("Ingrese superficie mínima: ")
    maximo = input("Ingrese superficie máxima: ")
    if not minimo.isdigit() or not maximo.isdigit():
        print("Valores inválidos.")
        return
    minimo = int(minimo)
    maximo = int(maximo)
    filtrados = []
    for p in paises:
        if p["superficie"] >= minimo and p["superficie"] <= maximo:
            filtrados.append(p)
    if len(filtrados) == 0:
        print("No hay países en ese rango de superficie.")
    else:
        for p in filtrados:
            mostrar_pais(p)

# Permite ordenar la lista de países por nombre, población o superficie
def ordenar_paises(paises):
    print("1) Nombre")
    print("2) Población")
    print("3) Superficie")
    op = input("Opción: ")
    print("a) Ascendente")
    print("b) Descendente")
    orden = input("Orden: ")

    descendente = False
    if orden.lower() == "b":
        descendente = True  # Si elige "b", ordena de mayor a menor

    # Ordena según la opción elegida
    if op == "1":
        paises.sort(key=lambda x: normalizar_texto(x["nombre"]), reverse=descendente)  # Ignora tildes y mayúsculas
    elif op == "2":
        paises.sort(key=lambda x: x["poblacion"], reverse=descendente)
    elif op == "3":
        paises.sort(key=lambda x: x["superficie"], reverse=descendente)
    else:
        print("Opción inválida.")
        return

    print("Países ordenados:")
    for p in paises:
        mostrar_pais(p)

# Calcula y muestra estadísticas sobre los países cargados
def estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_pob = 0
    total_sup = 0
    continentes = {}

    i = 0
    while i < len(paises):
        p = paises[i]
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

        # Busca el país con más y menos población
        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p

        # Cuenta cuántos países hay por continente
        cont = p["continente"]
        if cont not in continentes:
            continentes[cont] = 0
        continentes[cont] += 1
        i += 1

    # Calcula promedios
    prom_pob = total_pob / len(paises)
    prom_sup = total_sup / len(paises)

    # Muestra los resultados
    print("País con mayor población:", mayor_pob["nombre"], "-", mayor_pob["poblacion"])
    print("País con menor población:", menor_pob["nombre"], "-", menor_pob["poblacion"])
    print("Promedio de población:", int(prom_pob))
    print("Promedio de superficie:", int(prom_sup))
    print("Cantidad de países por continente:")
    for c in continentes:
        print(c, ":", continentes[c])

# Menú principal del programa
def menu():
    ruta = r"C:\Users\Joaco\Desktop\J\Facultad\Programacion\TP INTEGRADOR\paises.csv"
    paises = cargar_csv(ruta)  # Carga los datos del archivo
    opcion = ""
    while opcion != "7":  # Repite hasta que el usuario elija salir
        print("\n")
        print("====================")
        print(" GESTIÓN DE PAÍSES ")
        print("====================")
        print("\n1) Buscar país por nombre")
        print("2) Filtrar por continente")
        print("3) Filtrar por rango de población")
        print("4) Filtrar por rango de superficie")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("7) Salir")

        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1": buscar_pais(paises)
            case "2": filtrar_por_continente(paises)
            case "3": filtrar_por_poblacion(paises)
            case "4": filtrar_por_superficie(paises)
            case "5": ordenar_paises(paises)
            case "6": estadisticas(paises)
            case "7": print("Saliendo...")
            case _: print("Opción inválida")

# Llama al menú principal
menu()
