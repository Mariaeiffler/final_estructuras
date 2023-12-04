from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *

class Trabajo():
    def __init__(self,moneda,tipo_proy,estado,disciplina,proyectos,arbol):
        self.moneda=moneda
        self.tipo_proy=tipo_proy
        self.estado=estado
        self.disciplina=disciplina
        self.proyectos=proyectos
        self.arbol=diccionario_proy()

    def entrar(self): 
        obtener_pickle(self, 'abrir') 
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
        
if __name__ == "__main__":
    moneda,tipo_proy,estado,disciplina,proyectos,arbol=diccionario_proy()
    trabajo=Trabajo(moneda,tipo_proy,estado,disciplina,proyectos,arbol)
    trabajo.entrar()
