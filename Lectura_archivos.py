import csv
from Disciplina import Disciplina
from Estado_proyecto import Estado_proyecto
from Funcion import Funcion
from Moneda import Moneda
from Tipo_proyecto import Tipo_proyecto
from Proyecto import Proyecto


def leer_archivo(nombre):
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
    disciplinas = dict()
    for list in lista:
        dis = Disciplina(list[0],list[1],list[2],list[3],list[4],list[5],list[6])
        disciplinas[list[0]]=dis
    return disciplinas

def crear_clase_estado_proyecto(lista):
    estados_proy = dict()
    for list in lista:
        est = Estado_proyecto(list[0],list[1])
        estados_proy[list[0]]=est
    return estados_proy

def crear_clase_funcion(lista):
    funcion = dict()
    for list in lista:
        fun = Funcion(list[0],list[1])
        funcion[list[0]]=fun
    return funcion

def crear_clase_moneda(lista):
    moneda = dict()
    for list in lista:
        mon = Moneda(list[0],list[1],list[2])
        moneda[list[0]]=mon
    return moneda

def crear_clase_tipo_proyecto(lista):
    tipo_proy = dict()
    for list in lista:
        tipo = Tipo_proyecto(list[0],list[1],list[2],list[3],list[4])
        tipo_proy[list[0]]=tipo
    return tipo_proy

def crear_clase_proyecto(lista,moneda:dict,tipo_proy:dict,estado:dict,anio,disciplina:dict,proyectos:dict):
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
        match anio:
            case '2015':
                proyectos['2015'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion]=proy
            case '2016':
                proyectos['2016'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion]=proy
            case '2017':
                proyectos['2017'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion]=proy
            case '2018':
                proyectos['2018'][proy.disciplina.gran_area_descripcion][proy.disciplina.area_descripcion]=proy
    return proyectos

def crear_diccionario_proy_vacio(disciplina:dict):
    proyectos = {
        '2015':{},
        '2016':{},
        '2017':{},
        '2018':{}}
    setGranAreas=set()
    lista=list()
    dicc=dict()
    for key in disciplina:
        granArea=disciplina.get(key).gran_area_descripcion
        setGranAreas.add(granArea)
    for granAreaLlave in setGranAreas:
        dicc[granAreaLlave]={}
    for key in disciplina:
        if disciplina.get(key).area_descripcion not in lista:
            lista+=disciplina.get(key).gran_area_descripcion
            dicc[disciplina.get(key).gran_area_descripcion][disciplina.get(key).area_descripcion]=[]
    for keys in proyectos:
        proyectos[keys]=dicc
    return proyectos

def diccionario_proy():
    moneda = crear_clase_moneda(leer_archivo('ref_moneda.csv'))
    tipo_proy = crear_clase_tipo_proyecto(leer_archivo('ref_tipo_proyecto.csv'))
    estado = crear_clase_estado_proyecto(leer_archivo('ref_estado_proyecto.csv'))
    disciplina = crear_clase_disciplina(leer_archivo('ref_disciplina.csv')) 
    proyectosDicc=crear_diccionario_proy_vacio(disciplina)
    anio = 2015
    while anio <= 2018:
        nombre = 'proyectos_'+str(anio)+'.csv'
        proyectos=crear_clase_proyecto(leer_archivo(nombre),moneda,tipo_proy,estado,str(anio),disciplina,proyectosDicc)
        anio +=1
    return proyectos

if __name__=='__main__':
    
    print(diccionario_proy())

