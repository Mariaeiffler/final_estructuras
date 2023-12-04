import csv
from Disciplina import Disciplina
from Estado_proyecto import Estado_proyecto
from Funcion import Funcion
from Moneda import Moneda
from Tipo_proyecto import Tipo_proyecto
from Proyecto import Proyecto
from Arbol import *


def leer_archivo(nombre):
    '''Funcion para leer archivos de formato csv'''
    try:
        lista = []
        with open(nombre, 'r', encoding='utf-8') as archivo:  
            lector = csv.reader(archivo, delimiter=';')
            cont = 0           
            for fila in lector: 
                if cont != 0:
                    lista.append(fila)
                cont += 1
        return lista
    except FileNotFoundError:
        return
    
def crear_clase_disciplina(lista):
    '''La funcion crea los objetos de la clase disciplina y los agrega a un diccionario, que tiene como llave el id de la disciplina'''
    disciplinas = dict()
    for list in lista:
        dis = Disciplina(list[0],list[1],list[2],list[3],list[4],list[5],list[6])
        disciplinas[list[0]]=dis
    return disciplinas

def crear_clase_estado_proyecto(lista):
    '''La funcion crea los objetos de la clase estado_proyecto y los almacena en un diccionario, que tiene como llave el id del estado'''
    estados_proy = dict()
    for list in lista:
        est = Estado_proyecto(list[0],list[1])
        estados_proy[list[0]]=est
    return estados_proy

def crear_clase_funcion(lista):
    '''La funcion crea los objetos de la clase funcion y los almacena en un diccionario, que tiene como llave funcion_id'''
    funcion = dict()
    for list in lista:
        fun = Funcion(list[0],list[1])
        funcion[list[0]]=fun
    return funcion

def crear_clase_moneda(lista):
    '''La funcion crea los objetos de la clase moneda y los almacena en un diccionario, que tiene como llave moneda_id'''
    moneda = dict()
    for list in lista:
        mon = Moneda(list[0],list[1],list[2])
        moneda[list[0]]=mon
    return moneda

def crear_clase_tipo_proyecto(lista):
    '''La funcion crea los objetos de la clase tipo_proyecto y los almacena en un diccionario, que tiene como llave el id'''
    tipo_proy = dict()
    for list in lista:
        tipo = Tipo_proyecto(list[0],list[1],list[2],list[3],list[4])
        tipo_proy[list[0]]=tipo
    return tipo_proy

def crear_clase_proyecto(lista,moneda:dict,tipo_proy:dict,estado:dict,anio,disciplina:dict,proyectos:dict,arbol):
    '''La funcion crea los objetos de los proyectos y los guarda en el diccionario de proyectos (segun el año, gran area y subarea). Ademas, crea 
    el arbol para ordenar por fecha de inicio los distintos proyectos.'''
    lista_disciplinas = leer_archivo('proyecto_disciplina.csv')
    for proyecto in lista:
        for mon in moneda:
            if proyecto[6]==mon:
                id_mon = moneda.get(mon)
        for tipo in tipo_proy:
            if proyecto[11]==tipo:
                id_tipo_proy = tipo_proy.get(tipo)
        for est in estado:
            if proyecto[14]==est:
                id_estado = estado.get(est)
        for dis in lista_disciplinas:
            if dis[0]==proyecto[0]:
                if dis[1] == '0':
                    id_disciplina = disciplina.get('-1')
                else:
                    id_disciplina = disciplina.get(dis[1])
        
        proy = Proyecto(proyecto[0],proyecto[1],proyecto[2],proyecto[3],proyecto[4],proyecto[5],id_mon,proyecto[7],proyecto[8],proyecto[9],proyecto[10],id_tipo_proy,proyecto[12],proyecto[13],id_estado,proyecto[15],proyecto[16],proyecto[17],proyecto[18],anio,id_disciplina)
        arbol.insertar(proy)
        match anio:
            case '2015':
                proyectos['2015'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion].append(proy)
            case '2016':
                proyectos['2016'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion].append(proy)
            case '2017':
                proyectos['2017'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion].append(proy)
            case '2018':
                proyectos['2018'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion].append(proy)
    return proyectos,arbol

def crear_diccionario_proy_vacio(disciplina:dict):
    '''Esta funcion crea un diccionario de diccionarios donde se almacenaran todos los proyectos. El diccionario tiene como llaves los años de los 
    proyectos, las gran areas y las subareas. dentro del diccionario que tiene como llave las subareas se tiene una lista donde se van a almacenar los
    proyectos.'''
    proyectos = {
        '2015':{},
        '2016':{},
        '2017':{},
        '2018':{}}
    dicc,lista_vacia=conseguir_nombres(disciplina)
    for keys in proyectos:
        proyectos[keys]=dicc
    return proyectos

def diccionario_proy():
    '''La funcion crea los diccionarios del trabajo. Lee los distintos archivos y los devuelve para que puedan ser guardados en el pickle.  '''
    arbol=Arbol()
    moneda = crear_clase_moneda(leer_archivo('ref_moneda.csv'))
    tipo_proy = crear_clase_tipo_proyecto(leer_archivo('ref_tipo_proyecto.csv'))
    estado = crear_clase_estado_proyecto(leer_archivo('ref_estado_proyecto.csv'))
    disciplina = crear_clase_disciplina(leer_archivo('ref_disciplina.csv')) 
    proyectosDicc=crear_diccionario_proy_vacio(disciplina)
    anio = 2015
    while anio <= 2018:
        nombre = 'proyectos_'+str(anio)+'.csv'
        proyectos,arbol=crear_clase_proyecto(leer_archivo(nombre),moneda,tipo_proy,estado,str(anio),disciplina,proyectosDicc,arbol)
        anio +=1
    arbol.printear()
    return moneda,tipo_proy,estado,disciplina,proyectos,arbol

