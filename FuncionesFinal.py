import pickle
from datetime import *
# import matplotlib.pyplot as plt
import numpy as np

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
            
def anios_punto5():
    pregunta=input(('Elija de que anios quiere ver los proyectos: \n 1. 2015  \n 2. 2016 \n 3. 2017 \n 4. 2018 \n 5. todos \n'))
    imprimir = 'Error. Elija de que anios quiere ver los proyectos: \n 1. 2015  \n 2. 2016 \n 3. 2017 \n 4. 2018 \n 5. todos \n'
    pregunta=val_opc(pregunta,1,5,imprimir)
    anios = []
    match pregunta:
        case 1:
            anios.append(2015)
        case 2:
            anios.append(2016)
        case 3:
            anios.append(2017)
        case 4:
            anios.append(2018)
        case 5:
            anios.append(2015,2016,2017,2018)
    return anios

def proyectos_sin_repetir(proyectos:dict):
    proyectos_no_repetidos = set()
    for anio in proyectos.values():
        for gran_area in anio.values():
            for area in gran_area.values():
                for proyecto_particular in area:
                    proyectos_no_repetidos.add(proyecto_particular)
    return proyectos_no_repetidos

def porcentaje_hombres_mujeres(proyectos:dict):
    proyectos = proyectos_sin_repetir(proyectos)
    mujeres = 0
    hombres = 0
    for proyecto_particular in proyectos:
        if proyecto_particular.cantidad_miembros_F != '':
            mujeres += int(proyecto_particular.cantidad_miembros_F)
        if proyecto_particular.cantidad_miembros_M != '':
            hombres += int(proyecto_particular.cantidad_miembros_M)
    total = hombres + mujeres
    porcentaje_hombres = (hombres/total)*100
    porcentaje_mujeres = (mujeres/total)*100
    return porcentaje_mujeres , porcentaje_hombres

# def piechartpunto2(proyecto:dict):
#     mujeres, hombres = porcentaje_hombres_mujeres(proyecto)
#     porcentajes = np.array([hombres,mujeres])
#     labels = ["Hombres", "Mujeres"]
#     explode = [0.1,0]
#     colores = ['b','r']
#     titulo = 'Porcentajes de hombres y mujeres involucrados en proyectos'
#     plt.pie(porcentajes, explode = explode, startangle = 90, shadow = True, colors = colores)
#     plt.legend(labels)
#     plt.title(titulo, loc = 'center', pad = 20)
#     print('El porcentaje de participacion de mujeres es: ', mujeres, '%')
#     print ('El porcentaje de participacion de hombres es: ', hombres, '%')
#     plt.show() 


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

def relacion_monto(proyectos:dict):
    proyectos = proyectos_sin_repetir(proyectos)
    monto_solicitado = 0
    monto_otorgado = 0
    for proy in proyectos:
        monto_solicitado += float(proy.monto_financiado_solicitado)
        monto_otorgado += float(proy.monto_financiado_adjudicado)
    relacion = monto_otorgado/monto_solicitado
    try:
        with open('Relación_montos.txt', "w") as archivo:
            archivo.write('El monto total solicitado es: ')
            archivo.write(str(monto_solicitado))
            archivo.write('\n')
            archivo.write('El monto total otorgado es: ')
            archivo.write(str(monto_otorgado))
            archivo.write('\n')
            archivo.write('La relacion entre el monto otorgado y solicitado es: ')
            archivo.write(str(relacion))
    except Exception:
        pass
    
def visualizar_tiempo_promedio(trabajo):
    diccionario=trabajo.proyectos
    contador=0
    diferencia=0
    contador2=1
    diccionario_nombre={}
    imprimir="Error. Ingrese una opcion valida \n"
    no_uso,lista_nombres=conseguir_nombres(trabajo.disciplina)
    print("Las posibles subareas son:")
    for nombre_subarea in lista_nombres:
        print(f"{contador2}. {nombre_subarea}")
        diccionario_nombre[contador2] = nombre_subarea
        contador2+=1
    clave=input("\nIngrese el subarea que desea conocer su tiempo promedio de duracion\n")
    val_opc(clave,1,43,imprimir)
    subarea=diccionario_nombre[int(clave)]
    for año in diccionario.values():
        
        for gran_area in año.values():
            
            for area in gran_area:

                if subarea==area:
                    
                    lista_proyectos = gran_area[area]
                    for proyectos in lista_proyectos:
                        dif=0
                        fecha_inicio=datetime.strptime(proyectos.fecha_inicio, "%Y/%m/%d %H:%M:%S.%f")
                        fecha_final=datetime.strptime(proyectos.fecha_finalizacion, "%Y/%m/%d %H:%M:%S.%f")
                        dif=fecha_final-fecha_inicio

                        diferencia+=int(dif.days)
                        contador+=1
    if contador!=0:
        tiempo_prom=diferencia/contador
        try:
            with open('Tiempo_promedio.txt', "w") as archivo:
                archivo.write(f"El tiempo promedio del subarea {subarea} es de {tiempo_prom} dias")
        except Exception:
            pass


if __name__ == '__main__':
    print(menuPPL())