import pickle
from datetime import *

def obtener_pickle(trabajo, accion): #cambiar cuando sepamos 
    if accion == 'abrir':
        try:
            with open ('final.pickle','rb') as fpickle:
                info = pickle.load(fpickle)
            trabajo.proyectos=info.proyectos
            trabajo.arbol=info.arbol
            trabajo.moneda=info.moneda
            trabajo.tipo_proy=info.tipo_proy
            trabajo.estado=info.estado
            trabajo.disciplina=info.disciplina
            #agregar las cosas a cargar

        except FileNotFoundError:
            with open ('final.pickle','wb') as fpickle:
                pickle.dump(trabajo,fpickle)
    else:
        with open ('final.pickle','wb') as fpickle:
            pickle.dump(trabajo,fpickle)
        return

def val_int(x): 
    '''Esta función valida que sea un entero'''
    try:
        num=int(x)
        return True
    except Exception:
        return False
    
def val_opc(opcion, valor1, valor2, imprimir): 
    '''Esta función valida las opciones del menu principal '''
    validacion=False
    while validacion == False:
        if val_int(opcion):
            x=int(opcion)
            if x in range(valor1, valor2+1):
                validacion=True
            else:
                opcion = input(imprimir)
        else: 
            opcion = input(imprimir)
    return x

def menuPPL():
    pregunta=input(('Elija una de las siguientes opciones: \n 1. Mostrar la distribución de los proyectos por área de investigación y sus correspondientes sub áreas  \n 2. Visualizar el porcentaje de participación de las mujeres versus la participación de los hombres en los diferentes proyectos \n 3. Visualizar el tiempo promedio de terminación de los proyectos según el sub área al que pertenecen \n 4. Visualizar el porcentaje de los proyectos que han utilizado tecnologías emergentes \n 5. Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización \n 6. Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado \n 7. Salir del programa \n'))
    imprimir = 'Error. Elija una de las siguientes opciones: \n 1. Mostrar la distribución de los proyectos por área de investigación y sus correspondientes sub áreas  \n 2. Visualizar el porcentaje de participación de las mujeres versus la participación de los hombres en los diferentes proyectos \n 3. Visualizar el tiempo promedio de terminación de los proyectos según el sub área al que pertenecen \n 4. Visualizar el porcentaje de los proyectos que han utilizado tecnologías emergentes \n 5. Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización \n 6. Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado \n 7. Salir del programa \n'
    pregunta=val_opc(pregunta,1,7,imprimir)
    return pregunta

def convertirfecha_datetime(fecha):
    '''Esta función convierte una fecha dada en formato datetime'''
    validacion = False
    while validacion == False:
        try:
            fecha_datetime = datetime.strptime(fecha,'%Y/%m/%d %H:%M:%S.%f')
            validacion = True
            return fecha_datetime
        except Exception:
            print('no se convirtio')

def conseguir_nombres(disciplina:dict):
    setGranAreas=set()
    lista=list()
    dicc=dict()
    lista_subareas=[]
    for key in disciplina:
        granArea=disciplina.get(key).gran_area_descripcion
        setGranAreas.add(granArea)
    for granAreaLlave in setGranAreas:
        dicc[granAreaLlave]={}
    for key in disciplina:
        if disciplina.get(key).area_descripcion not in lista:
            dicc[disciplina.get(key).gran_area_descripcion][disciplina.get(key).area_descripcion]=[]
        if disciplina.get(key).area_descripcion not in lista_subareas:
            lista_subareas.append(disciplina.get(key).area_descripcion)
    return dicc,lista_subareas


if __name__ == '__main__':
    print(menuPPL())