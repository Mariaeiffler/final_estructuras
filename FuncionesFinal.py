import pickle
from datetime import *
import matplotlib.pyplot as plt
import numpy as np

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
    '''Esta funcion pide los años que se quieren visualizar en el punto 5 del menu.'''
    pregunta=input(('Elija de que anios quiere ver los proyectos: \n 1. 2015  \n 2. 2016 \n 3. 2017 \n 4. 2018 \n 5. todos \n'))
    imprimir = 'Error. Elija de que anios quiere ver los proyectos: \n 1. 2015  \n 2. 2016 \n 3. 2017 \n 4. 2018 \n 5. todos \n'
    pregunta=val_opc(pregunta,1,5,imprimir)
    anios = set()
    match pregunta:
        case 1:
            anios.add(2015)
        case 2:
            anios.add(2016)
        case 3:
            anios.add(2017)
        case 4:
            anios.add(2018)
        case 5:
            anios.add(2015)
            anios.add(2016)
            anios.add(2017)
            anios.add(2018)
    print(anios)
    return anios

def proyectos_sin_repetir(proyectos:dict):
    '''Esta funcion crea un set con todos los proyectos. Se suele usar para sacar los proyectos que estan repetidos en el diccionario de proyectos.'''
    proyectos_no_repetidos = set()
    for anio in proyectos.values():
        for gran_area in anio.values():
            for area in gran_area.values():
                for proyecto_particular in area:
                    proyectos_no_repetidos.add(proyecto_particular)
    return proyectos_no_repetidos

def porcentaje_hombres_mujeres(proyectos:dict):
    '''Esta funcion calcula el porcentaje de hombres y mujeres trabajando en todos los proyectos. Se utiliza para el punto 2 del menu.'''
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


def conseguir_nombres(disciplina:dict):
    '''Esta funcion crea el diccionario de diccionarios ordenado por area y subarea, que despues se agrega al diccionario de proyectos según el año
    y crea una lista con la descripcion de las subareas. Para lograr esto se utiliza un set para que las gran areas no se repitan y se cree el diccionario
    correctamente cuando se quiera utilizar la descripcion como llave. '''
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
    '''Esta función realiza el punto 6 del menu. Crea un archivo con la relación de monto solicitado y otorgado, recorriendo el 
    set que contiene los proyectos, obteniendo de los distintos objetos los valores necesitados e visualizandolos en un txt'''
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
    '''Esta funcion realiza el punto 3 del menu. Permite visualizar el tiempo promedio que tarda el proyecto seleccionado en 
    en dias en realizarse. Utiliza datetime para poder convertir las fechas al formato necesario y hacer la diferencia. Los resultados
    se imprimen en un archivo de formato txt.'''
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
    clave=val_opc(clave,1,43,imprimir)
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
                archivo.write(f"El tiempo promedio del subarea '{subarea}' es de {tiempo_prom} dias")
        except Exception:
            pass

def tecnologias_emergentes(proyectos:dict):
    '''Esta funcion hace el punto '''
    proyectos = proyectos_sin_repetir(proyectos)
    lista = []
    for proy in proyectos:
        if proy.tipo_proyecto_id.tipo_proyecto_cyt_id == '2':
            lista.append(proy)
    porcentaje = (len(lista)/len(proyectos))*100
    try:
        with open('Tecnologias_emergentes.txt', "w") as archivo:
            archivo.write(f'El porcentaje de proyectos que usaron tecnologias emergentes es: {porcentaje} %')
    except Exception:
        pass
    
def porcentaje_areas(trabajo):
    lista_listas = []
    lista_areas = []
    cantidades = []
    lista_proyec = set()
    for anio in trabajo.proyectos.values():
        for gran_area in anio.values():
            for area in gran_area.values():
                for proyecto_particular in area:
                    lista_proyec.add(proyecto_particular)
    for proyec in lista_proyec:
        if proyec.disciplina.gran_area_descripcion not in lista_areas:
                lista_areas.append(proyec.disciplina.gran_area_descripcion)
                lista_listas.append([proyec.disciplina.gran_area_descripcion, 1])
        else:
            for lista in lista_listas:
                if lista[0] == proyec.disciplina.gran_area_descripcion:
                    lista[1] += 1           
    total = len(lista_proyec)
    for lista in lista_listas:
        cantidades.append(lista[1])
    cant = np.array(cantidades)
    porcentajes = (cant/total)*100     
    return porcentajes, lista_areas

def porcentaje_subareas(trabajo):
    lista_listas = []
    lista_subareas = []
    cantidades = []
    contador = 0
    lista_areas = ['SIN DATOS', 'CIENCIAS NATURALES Y EXACTAS', 'CIENCIAS MEDICAS Y DE LA SALUD', 'INGENIERIAS Y TECNOLOGIAS','CIENCIAS AGRICOLAS' ,'CIENCIAS SOCIALES','HUMANIDADES']
    print('Las siguientes son las areas de investigación:')
    for l in lista_areas:
        print(l)
    aprobado = True
    while aprobado:
        g_area = input('Ingrese el area en la que quiera mostrar la distrbucion de los proyectos \n')
        g_area = g_area.upper()
        for i in lista_areas:
            if i == g_area:
                aprobado = False
    proyectos = trabajo.proyectos
    for anio in proyectos.values():
        for gran_area in anio.values():
            for area in gran_area.values():
                for proyecto_particular in area:
                    if proyecto_particular.disciplina.gran_area_descripcion == g_area:
                        if proyecto_particular.disciplina.area_descripcion not in lista_subareas:
                            lista_subareas.append(proyecto_particular.disciplina.area_descripcion)
                            lista_listas.append([proyecto_particular.disciplina.area_descripcion, 1])
                        else:
                            for lista in lista_listas:
                                if lista[0] == proyecto_particular.disciplina.area_descripcion:
                                    lista[1] += 1 
                        contador += 1
    
    for lista in lista_listas:
        cantidades.append(lista[1])
    cant = np.array(cantidades)
    porcentajes = (cant/contador)*100     
    return porcentajes, lista_subareas, g_area

def piecharts_subareas(trabajo):
    porcentajes, lista_subareas, area = porcentaje_subareas(trabajo)
    titulo = "Distribucion de los proyectos segun el subarea de investigacion del area:" + area
    plt.pie(porcentajes, labels = None,  startangle = 180)
    plt.title(titulo, loc = 'center', pad= 20)
    plt.legend(lista_subareas,  title="Subáreas", bbox_to_anchor=(1, 0.5), loc="center left", fontsize='small')
    plt.show()
    
def piechartpunto1(trabajo):
    porcentajes, lista_areas = porcentaje_areas(trabajo)
    titulo = "Distribución de los proyectos por Area de investigación"
    plt.pie(porcentajes, labels = lista_areas,  startangle = 180,autopct='%1.1f%%', pctdistance=0.85)
    plt.title(titulo, loc = 'center', pad= 20)
    plt.show()
    
def piechartpunto2(proyectos:dict):
    mujeres, hombres = porcentaje_hombres_mujeres(proyectos)
    porcentajes = np.array([hombres,mujeres])
    labels = ["Hombres", "Mujeres"]
    explode = [0.1,0]
    colores = ['b','r']
    titulo = 'Porcentajes de hombres y mujeres involucrados en proyectos'
    plt.pie(porcentajes, explode = explode, startangle = 90, shadow = True, colors = colores, autopct='%1.1f%%', pctdistance=0.85)
    plt.legend(labels)
    plt.title(titulo, loc = 'center', pad = 20)
    print('El porcentaje de participacion de mujeres es: ', mujeres, '%')
    print ('El porcentaje de participacion de hombres es: ', hombres, '%')
    plt.show() 

