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
                    piechartpunto1(self)
                    piecharts_subareas(self)
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

    
    def porcentaje_areas(self):
        proyectos = self.proyectos
        lista_listas = []
        lista_areas = []
        cantidades = []
        lista_proyec = set()
        for anio in proyectos.values():
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

    def porcentaje_subareas(self):
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
            g_area = input('Ingrese el area en la que quiera mostrar la distrbucion de los proyectos')
            g_area = g_area.upper()
            for i in lista_areas:
                if i == g_area:
                    aprobado = False
        proyectos = self.proyectos
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
        print(cantidades)
        cant = np.array(cantidades)
        porcentajes = (cant/contador)*100     
        return porcentajes, lista_subareas, g_area

def piecharts_subareas(trabajo):
    porcentajes, lista_subareas, area = trabajo.porcentaje_subareas()
    titulo = "Distribucion de los proyectos segun el subarea de investigacion del area:" + area
    piechart = plt.pie(porcentajes, labels = lista_subareas,  startangle = 90)
    plt.title(titulo, loc = 'center', pad= 20)
    plt.setp(piechart[1], fontsize=8)
    plt.show()

def obtener_pickle(): #cambiar cuando sepamos 
    try:
        with open ('final.pickle','rb') as fpickle:
            trabajo = pickle.load(fpickle)

    except FileNotFoundError:
        moneda,tipo_proy,estado,disciplina,proyectos,arbol=diccionario_proy()
        trabajo=Trabajo(moneda,tipo_proy,estado,disciplina,proyectos,arbol)
        with open ('final.pickle','wb') as fpickle:
            pickle.dump(trabajo,fpickle)
    return trabajo
    
def piechartpunto1(trabajo):
    porcentajes, lista_areas = trabajo.porcentaje_areas()
    titulo = "Distribución de los proyectos por Area de investigación"
    plt.pie(porcentajes, labels = lista_areas,  startangle = 180,autopct='%1.1f%%', pctdistance=0.85)
    plt.title(titulo, loc = 'center', pad= 20)
    plt.show()
    

        
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
    obtener_pickle().entrar()

    