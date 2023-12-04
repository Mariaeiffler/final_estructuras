from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *
from datetime import datetime as dt
import numpy as np
# import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(5000)

class Trabajo():
    def __init__(self,moneda,tipo_proy,estado,disciplina,proyectos,arbol):
        self.moneda=moneda
        self.tipo_proy=tipo_proy
        self.estado=estado
        self.disciplina=disciplina
        self.proyectos=proyectos
        self.arbol=arbol
        
    def entrar(self):  
        seguir = True
        pregunta=menuPPL()
        while seguir==True: 
            match pregunta:
                case 1:
                    '''Mostrar la distribución de los proyectos por área de investigación y sus correspondientes sub áreas'''
                    print(proyectos.get('2018'))
                    pregunta=menuPPL()
                case 2:
                    '''Visualizar el porcentaje de participación de las mujeres versus la participación de los hombres en los diferentes proyectos'''
                    print(self.porcentaje_hombres_mujeres())
                    pregunta=menuPPL()
                case 3:
                    '''Visualizar el tiempo promedio de terminación de los proyectos según el sub área al que pertenecen'''
                    pregunta=menuPPL() 
                case 4:
                    '''Visualizar el porcentaje de los proyectos que han utilizado tecnologías emergentes'''
                    pregunta=menuPPL()
                case 5:
                    '''Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización'''
                    anios = anios_punto5()
                    self.arbol.recorrer_en_orden(anios)
                    pregunta=menuPPL()
                    
                case 6:
                    '''Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado'''
                    pregunta=menuPPL()
                case 7:
                    seguir=False   
        print('Se ha cerrado el programa con éxito.')

    def proyectos_sin_repetir(self):
        proyectos = self.proyectos
        proyectos_no_repetidos = set()
        for anio in proyectos.values():
            for gran_area in anio.values():
                for area in gran_area.values():
                    for proyecto_particular in area:
                        proyectos_no_repetidos.add(proyecto_particular)
        return proyectos_no_repetidos
        

    def porcentaje_hombres_mujeres(self):
        proyectos = self.proyectos_sin_repetir()
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
    
    def visualizar_tiempo_promedio(self):
        diccionario=self.proyectos
        contador=0
        diferencia=0
        contador2=1
        diccionario_nombre={}
        imprimir="Error. Ingrese una opcion valida"
        no_uso,lista_nombres=conseguir_nombres(self.disciplina)
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
                            fecha_inicio=dt.strptime(proyectos.fecha_inicio, "%Y/%m/%d %H:%M:%S.%f")
                            fecha_final=dt.strptime(proyectos.fecha_finalizacion, "%Y/%m/%d %H:%M:%S.%f")
                            dif=fecha_final-fecha_inicio

                            diferencia+=int(dif.days)
                            contador+=1
        if contador!=0:
            tiempo_prom=diferencia/contador
            print(f"El tiempo promedio del subarea {subarea} es de {tiempo_prom} dias")
        

  
if __name__ == "__main__":
    trabajo=Trabajo()
    trabajo.visualizar_tiempo_promedio()
def obtener_pickle(): #cambiar cuando sepamos 
    try:
        with open ('final.pickle','rb') as fpickle:
            trabajo = pickle.load(fpickle)
        #agregar las cosas a cargar

    except FileNotFoundError:
        moneda,tipo_proy,estado,disciplina,proyectos,arbol=diccionario_proy()
        trabajo=Trabajo(moneda,tipo_proy,estado,disciplina,proyectos,arbol)
        with open ('final.pickle','wb') as fpickle:
            pickle.dump(trabajo,fpickle)
    return trabajo

    
        
# def piechartpunto2(trabajo):
#     mujeres, hombres = trabajo.porcentaje_hombres_mujeres()
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


if __name__ == "__main__":
    obtener_pickle().entrar()


