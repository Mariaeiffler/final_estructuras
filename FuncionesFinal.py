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

if __name__ == '__main__':
    print(menuPPL())