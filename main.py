from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *
from datetime import datetime as dt
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
                    pregunta=menuPPL()
                case 2:
                    '''Visualizar el porcentaje de participación de las mujeres versus la participación de los hombres en los diferentes proyectos'''
                    print(porcentaje_hombres_mujeres(self.proyectos))
                    # piechartpunto2(self.proyectos)
                    pregunta=menuPPL()
                case 3:
                    '''Visualizar el tiempo promedio de terminación de los proyectos según el sub área al que pertenecen'''
                    visualizar_tiempo_promedio(self)
                    print('Se ha creado un archivo con la información que desea visualizar \n')
                    pregunta=menuPPL() 
                case 4:
                    '''Visualizar el porcentaje de los proyectos que han utilizado tecnologías emergentes'''
                    tecnologias_emergentes(self.proyectos)
                    pregunta=menuPPL()
                case 5:
                    '''Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización'''
                    anios = anios_punto5()
                    self.arbol.recorrer_en_orden(anios)
                    print('Se ha creado un archivo con la información que desea visualizar \n')
                    pregunta=menuPPL()
                    
                case 6:
                    '''Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado'''
                    relacion_monto(self.proyectos)
                    print('Se ha creado un archivo con la información que desea visualizar \n')
                    pregunta=menuPPL()
                case 7:
                    seguir=False   
        print('Se ha cerrado el programa con éxito.')        
        
def obtener_pickle():
    try:
        with open ('final.pickle','rb') as fpickle:
            trabajo = pickle.load(fpickle)

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


