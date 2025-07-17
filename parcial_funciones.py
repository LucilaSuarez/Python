import json

'''Apellido y nombre: Lucila Micaela Suarez '''

def cargar_datos(path: str):
    '''Recibe por parametros el archivo, lo abre en modo lectura y nos informa si este fue cargado o no correctamente '''
    with open(path, 'r') as archivo: 
        datos = json.load(archivo) 
    print("Datos cargados correctamente")
    return datos['juegos']

def guardar_datos(lista: list, path: str):
    '''Recibe por parametros una lista y un archivo. Lo abre en modo escritura y guarda la lista en el archivo '''
    with open (path, 'w') as archivo:
        json.dump({"juegos":lista}, archivo, indent = 4)

def alta_datos(juegos):
    ''' Recibe por parametros una lista. Se piden los datos del nuevo juego y lo almacena en el diccionario de juegos'''
    nuevo_id = len(juegos) + 1
    nombre = input("Ingrese nombre del juego: ")
    while len(nombre) > 30:
        nombre = input("ERROR, solo se permiten 30 caracetres. Reingrese nombre")
    empresa = input("Ingrese empresa: ")
    while empresa != "Namco" and empresa != "Taito" and empresa != "Nintendo" and empresa !=  "Atari" and empresa != "Sega" and empresa != "Konami" and empresa != "Capcom" and empresa != "Epic Games":
        empresa = input("ERROR, reingrese empresa:")
    anio = int(input("Ingrese año:"))
    while anio < 1978 or anio > 2024:
        anio = int(input("ERROR, Reingrese año"))
    genero = input("Ingrese genero: ")
    while genero != "Laberinto" and genero != "Puzzle" and genero != "Plataformas" and genero != "Peleas" and genero !=  "Matamarcianos" and genero !=  "Disparos" and genero != "Carreras":
        genero = input("ERROR, Reingrese genero:")
    nuevo_juego = {
        "id" : nuevo_id,
        "nombre": nombre,
        "empresa": empresa,
        "anio": str(anio),
        "genero": genero
        }
    juegos.append(nuevo_juego)
    guardar_datos (juegos, "/Users/lulis/OneDrive/Escritorio/Curso_de_ingreso_PYTHON/Progrmacion1/data.json")
    print("Juego nuevo guardado correctamente")

def modificar_datos (juegos):
    '''Recibe por parametros una lista, se pide un id y luego modifica los datos que el usuario desee del juego con ese id'''
    encabezado = "ID  |  Nombre  "
    print (encabezado)
    juego_a_modificar = None
    for juego in juegos:
        mensaje = ""
        for datos in juego: 
            mensaje = f"{juego ['id']:}  |  {juego['nombre']}"
        print (mensaje) 
    id_a_modificar = int(input("Ingrese ID del juego que desea modificar: "))
    for juego in juegos:
        if juego["id"] == id_a_modificar:
            juego_a_modificar = juego
            break
    sub_menu = input("Que desea modificar.\nA. Nombre\nB. Empresa\nC. Año\nIngrese opcion: ")
    match sub_menu:
        case "A":
            nuevo_nombre = input("Ingrese el nuevo nombre: ").capitalize()
            while len(nuevo_nombre) > 30:
                nuevo_nombre = input("ERROR, solo se permiten 30 caracetres. Reingrese nombre").capitalize()
            juego_a_modificar["nombre"] = nuevo_nombre
        case "B":
            nueva_empresa = input("Ingrese la nueva empresa: ").capitalize()
            while nueva_empresa != "Namco" and nueva_empresa != "Taito" and nueva_empresa != "Nintendo" and nueva_empresa !=  "Atari" and nueva_empresa != "Sega" and nueva_empresa != "Konami" and nueva_empresa != "Capcom" and nueva_empresa != "Epic Games":
                nueva_empresa = input("ERROR, reingrese empresa:").capitalize()
            juego_a_modificar["empresa"] = nueva_empresa
        case "C":
            nuevo_anio =  int(input("Ingrese el nuevo año: "))
            while nuevo_anio < 1978 or nuevo_anio > 2024:
                nuevo_anio = int(input("ERROR, Reingrese año"))
            juego_a_modificar["anio"] = str(nuevo_anio)
        case _:
            print("Opcion invalida")
    guardar_datos (juegos, "/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/data.json")
    print("Datos modificados correctamente")

def borrar_datos (juegos):
    ''' Recibe por parametros una lista, y nos imprime la lista (solo su id y nombre), el usuario ingresa el id del juego que desea eliminar y este se elimina. '''
    encabezado = "ID  |  Nombre  "
    print (encabezado)
    for juego in juegos:
        mensaje = ""
        for datos in juego: 
            mensaje = f"{juego ['id']:}  |  {juego['nombre']}"
        print (mensaje) 
    juego_a_elimar = None
    id_ingresado = int(input("Ingrese id del juego que desea eliminar: "))
    for juego in juegos:
        if juego['id'] == id_ingresado:
            juego_a_elimar = juego
            break
    if juego_a_elimar:
        juegos.remove(juego_a_elimar)
        guardar_datos (juegos, "/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/data.json")
        print(f"Juego con ID {id_ingresado} eliminado correctamente.")
    else:
        print(f"No se encontró un juego con ID {id_ingresado}")

def listar_datos (juegos):
    ''' Reccibe por parmetros una lista y nos retorna sus datos, menos el id, de manera ordenada'''
    encabezado = print ("Nombre             |", "Empresa       |" , "Año      |", "Genero")
    for juego in juegos:
        nombre = juego['nombre']
        empresa = juego['empresa']
        anio = juego['anio']
        genero = juego['genero']
        mensaje = print (f"{nombre:20} {empresa:15} {anio:10} {genero:15}")
    guardar_datos (juegos, "/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/data.json")

def listar_datos_peleas (juegos):
    ''' Recibe por parametros una lista y nos retorna una nueva solo con los juegos cuyo genero sea pelea'''
    encabezado = print ("Nombre             |", "Empresa       |" , "Año      |", "Genero")
    lista_peleas = []
    for juego in juegos:
        if juego['genero'] == "Peleas":
            lista_peleas.append(juego)
            nombre = juego['nombre']
            empresa = juego['empresa']
            anio = juego['anio']
            genero = juego['genero']
            print(f"{nombre:20} {empresa:15} {anio:10} {genero:15}")
    return lista_peleas

def filtar_datos_por_año(juegos):
    '''Recibe por parametros una lista y nos retorna la cantidad de datos que tiene segun el rango de años que ingreso el usuario '''
    desde_anio = int(input("Ingrese desde que año desea ver los juegos: "))
    while desde_anio < 1978 or desde_anio > 2024:
        desde_anio = int(input("ERROR, Reingrese año:"))
    hasta_anio = int(input("Ingrese hasta que año desea ver los juegos: "))
    while hasta_anio < 1978 or hasta_anio > 2024:
        hasta_anio = int(input("ERROR, Reingrese año:"))
    contador = 0
    for juego in juegos:
        if desde_anio <= int(juego['anio']) and hasta_anio >= int(juego['anio']):
            contador += 1
    print(f"Se encontraron {contador} juegos entre los años {desde_anio} y {hasta_anio}")
    return contador

def ordenar(lista: list, clave: str ):
    '''Recibe por parametros una lista y una clave que segun esta clave ordena los datos de manera ascendente o desendente '''
    indicador = input("Desea ordenar los datos de manera asendente (asc) o desentende (des): ")
    if indicador == "asc":
        for i in range(len(lista)-1): 
            for j in range(i+1 ,len(lista)):
                if lista[i][clave] > lista[j][clave]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        print(f"Juegos ordenados por {clave} ascendentemente:")
        encabezado = print ("Nombre             |", "Empresa       |" , "Año      |", "Genero")
        for juego in lista:
            nombre = juego['nombre']
            empresa = juego['empresa']
            anio = juego['anio']
            genero = juego['genero']
            print(f"{nombre:20} {empresa:15} {anio:10} {genero:15}") 

    elif indicador == "des":
        for i in range(len(lista)-1): 
            for j in range(i+1, len(lista)):
                if  lista[i][clave] < lista[j][clave]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        print(f"Juegos ordenados por {clave} desendentemente:")
        encabezado = print ("Nombre             |", "Empresa       |" , "Año      |", "Genero")
        for juego in lista:
            nombre = juego['nombre']
            empresa = juego['empresa']
            anio = juego['anio']
            genero = juego['genero']
            print(f"{nombre:20} {empresa:15} {anio:10} {genero:15}") 

def exportar_csv(lista: list, path: str):
    ''' Recibe por parametros una lista y guarda sus datos en un archivo csv'''
    with open(path, "w") as archivo:
        for linea in lista:
            archivo.write(f"{linea["nombre"]}, {linea["empresa"]}, {linea["anio"]}, {linea["genero"]},\n")
    print(f"Los juegos se guardaron correctamente")

def calcular_max_min(lista: list, clave: str, indicador: str):
    juegos_resultado = []
    valor_extremo = None

    for juego in lista:
        valor_actual = float(juego[clave])

        if valor_extremo is None:
            valor_extremo = valor_actual
            juegos_resultado = [juego]
        elif indicador == "min":
            if valor_actual < valor_extremo:
                valor_extremo = valor_actual
                juegos_resultado = [juego]
            elif valor_actual == valor_extremo:
                juegos_resultado.append(juego)
        elif indicador == "max":
            if valor_actual > valor_extremo:
                valor_extremo = valor_actual
                juegos_resultado = [juego]
            elif valor_actual == valor_extremo:
                juegos_resultado.append(juego)

    print("\nNombre             | Empresa        | Año       | Genero")
    for juego in juegos_resultado:
        print(f"{juego['nombre']:20} {juego['empresa']:15} {juego['anio']:10} {juego['genero']:15}")
    return juegos_resultado

# Listar por pantalla todos los juegos de una empresa y género determinados. El usuario deberá ingresar por consola la Empresa y el Género.
def agrupar_empresa(lista: list):
    empresa_agrupar = input("Ingrese el nombre de la empresa que desea agrupar: ")
    while empresa_agrupar != "Namco" and empresa_agrupar != "Taito" and empresa_agrupar != "Nintendo" and empresa_agrupar !=  "Atari" and empresa_agrupar != "Sega" and empresa_agrupar != "Konami" and empresa_agrupar != "Capcom" and empresa_agrupar != "Epic Games":
        empresa_agrupar = input("ERROR, reingrese empresa:")
    genero_agrupar = input("Ingrese genero por el que desea agrupar: ")
    while genero_agrupar != genero_agrupar != "Laberinto" and genero_agrupar != "Puzzle" and genero_agrupar != "Plataformas" and genero_agrupar != "Peleas" and genero_agrupar !=  "Matamarcianos" and genero_agrupar !=  "Disparos" and genero_agrupar != "Carreras":
        genero_agrupar = input("ERROR, Reingrese genero:")
    empresa_genero_lista = []
    encabezado = print ("Nombre             |", "Empresa       |" , "Año      |", "Genero")
    for juego in lista:
        if juego['empresa'] == empresa_agrupar and juego['genero'] == genero_agrupar:
            empresa_genero_lista.append(juego)
            nombre = juego['nombre']
            empresa = juego['empresa']
            anio = juego['anio']
            genero = juego['genero']
            print(f"{nombre:20} {empresa:15} {anio:10} {genero:15}") 
    return empresa_genero_lista 
