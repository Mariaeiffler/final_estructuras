from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *
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
    
def obtener_pickle(accion,trabajo=None): #cambiar cuando sepamos 
    if accion == 'abrir':
        try:
            # trabajo = Trabajo(None,None,None,None,None,None)
            with open ('final.pickle','rb') as fpickle:
                trabajo = pickle.load(fpickle)
            # trabajo.proyectos=info.proyectos
            # trabajo.arbol=info.arbol
            # trabajo.moneda=info.moneda
            # trabajo.tipo_proy=info.tipo_proy
            # trabajo.estado=info.estado
            # trabajo.disciplina=info.disciplina
            #agregar las cosas a cargar

        except FileNotFoundError:
            moneda,tipo_proy,estado,disciplina,proyectos,arbol=diccionario_proy()
            trabajo=Trabajo(moneda,tipo_proy,estado,disciplina,proyectos,arbol)
            with open ('final.pickle','wb') as fpickle:
                pickle.dump(trabajo,fpickle)
        return trabajo
    # else:
    #     with open ('final.pickle','wb') as fpickle:
    #         pickle.dump(trabajo,fpickle)
    
        
if __name__ == "__main__":
    trabajo = obtener_pickle('abrir')
    trabajo.entrar()
    print(trabajo.proyectos)
    print(trabajo.porcentaje_hombres_mujeres())
    # obtener_pickle('cerrar',trabajo)

