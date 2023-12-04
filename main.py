from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *
import numpy as np
import matplotlib.pyplot as plt

class Trabajo():
    def __init__(self):
        self.moneda,self.tipo_proy,self.estado,self.disciplina,self.proyectos,self.arbol=diccionario_proy()

    def entrar(self): 
        obtener_pickle(self, 'abrir') 
        seguir = True
        pregunta=menuPPL()
        while seguir==True: 
            match pregunta:
                case 1:
                    '''Mostrar la distribución de los proyectos por área de investigación y sus correspondientes sub áreas'''
                    pregunta=menuPPL()
                case 2:
                    '''Visualizar el porcentaje de participación de las mujeres versus la participación de los hombres en los diferentes proyectos'''
                    pregunta=menuPPL()
                case 3:
                    '''Visualizar el tiempo promedio de terminación de los proyectos según el sub área al que pertenecen'''
                    pregunta=menuPPL() 
                case 4:
                    '''Visualizar el porcentaje de los proyectos que han utilizado tecnologías emergentes'''
                    pregunta=menuPPL()
                case 5:
                    '''Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización'''
                    pregunta=menuPPL()
                case 6:
                    '''Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado'''
                    pregunta=menuPPL()
                case 7:
                    seguir=False   
                           
        obtener_pickle(self, 'cerrar') 
        print('Se ha cerrado el programa con éxito.')

    def porcentaje_hombres_mujeres(self):
        proyectos = self.proyectos
        mujeres = 0
        hombres = 0
        for anio in proyectos.values():
            for gran_area in anio.values():
                for area in gran_area.values():
                    for proyecto_particular in area:
                        if proyecto_particular.cantidad_miembros_F != '':
                            mujeres += int(proyecto_particular.cantidad_miembros_F)
                        if proyecto_particular.cantidad_miembros_M != '':
                            hombres += int(proyecto_particular.cantidad_miembros_M)
        total = hombres + mujeres
        porcentaje_hombres = (hombres/total)*100
        porcentaje_mujeres = (mujeres/total)*100
        return porcentaje_mujeres , porcentaje_hombres

        
def piechartpunto2(trabajo):
    mujeres, hombres = trabajo.porcentaje_hombres_mujeres()
    porcentajes = np.array([hombres,mujeres])
    labels = ["Hombres", "Mujeres"]
    explode = [0.1,0]
    colores = ['b','r']
    titulo = 'Porcentajes de hombres y mujeres involucrados en proyectos'
    plt.pie(porcentajes, explode = explode, startangle = 90, shadow = True, colors = colores)
    plt.legend(labels)
    plt.title(titulo, loc = 'center', pad = 20)
    print('El porcentaje de participacion de mujeres es: ', mujeres, '%')
    print ('El porcentaje de participacion de hombres es: ', hombres, '%')
    plt.show() 


if __name__ == "__main__":
    trabajo=Trabajo()
    trabajo.entrar()

