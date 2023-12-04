from FuncionesFinal import *
from Arbol import *
from Lectura_archivos import *

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
        
if __name__ == "__main__":
    trabajo=Trabajo()
    trabajo.entrar()