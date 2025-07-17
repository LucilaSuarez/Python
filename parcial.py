import json
from parcial_funciones import *

'''Apellido y nombre: Lucila Micaela Suarez '''

continuar = True
carga_datos = False
juegos_peleas = False
juegos_ordenados = False
#juegos = []

while continuar == True:
    menu = input("\n == Menu == \n\nA. Cargar Datos\nB. Alta de datos\nC. Modificar datos\nD. Borrar datos\nE. Listar datos\nF. Sub-Menu\nG. Sub-Menu.\nH. Salir\nIngrese opcion: ")
    match menu:
        case "A":
            juegos = cargar_datos("/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/data.json")
            carga_datos = True
        case "B":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else: 
                alta_datos(juegos)
        case "C":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else:
                modificar_datos(juegos)
        case "D":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else: 
                borrar_datos (juegos)
        case "E":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else:
                listar_datos(juegos)
        case "F":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else:
                menu_2 = input(" == Sub-Menu == \n\n1. Listar por pantalla los juegos cuyo género sea Peleas\n2. Mostrar la cantidad de juegos de un rango de años determinado (año desde y año hasta)\n3. Listar todos los juegos ordenados por Empresa (asc/des)\n4. Exportar a JSON la lista de juegos\n5. Expotar a CSV la lista ordenada (asc/des)\nIngrese opcion: ")
                match menu_2:
                    case "1":
                        if juegos_peleas == False:
                            listar_datos_peleas(juegos)
                            juegos_peleas = True
                    case "2":
                        filtar_datos_por_año(juegos)
                    case "3":
                        if juegos_ordenados == False:
                            ordenar (juegos, 'empresa')
                            juegos_ordenados = True
                    case "4":
                        if juegos_peleas == False:
                            print("Es necesario que primero se obtengan los juegos cuyo genero sea Pelea. Porfavor seleccione la opcion 1")
                        else:
                            lista_peleas = listar_datos_peleas(juegos)
                            guardar_datos(lista_peleas, "/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/F4.json")
                            print("Los juegos se guardaron correctamente")
                    case "5":
                        if juegos_ordenados == False:
                            print("Es necesario que primero se ordenen los juegos.Por favor seleccione la opcion 3")
                        else:
                            exportar_csv(juegos,"/Users/lulis/OneDrive/Escritorio/Progrmacion I/Python/F5.csv" )
        case "G":
            if carga_datos == False:
                print("Primero se deben cargar los datos, Ingrese la opcion A")
            else:
                menu_3 = input(" == Sub-Menu == \n1. Listar por pantalla el/los juego/s más antiguo/s y más nuevo/s.\n2. Listar por pantalla todos los juegos de una empresa y género determinados.\nIngrese opcion:")
                match menu_3:
                    case "1":
                        calcular_max_min(juegos, 'anio', "min")
                        calcular_max_min(juegos, 'anio', "max")
                    case "2":
                        agrupar_empresa(juegos)
        case "H":
            continuar = False
        case _:
            print ("Opcion invalida")
print ("Programa finalizado")