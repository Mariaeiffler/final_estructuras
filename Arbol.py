from Proyecto import *
from FuncionesFinal import *
from Nodo import *
from datetime import *

class Arbol:
    def __init__(self,raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, raiz, valor):
        if raiz is None:
            return Nodo(valor)
        else:
            if convertirfecha_datetime(valor.fecha_inicio) <= convertirfecha_datetime(raiz.valor.fecha_inicio):
                raiz.izquierda = self._insertar(raiz.izquierda, valor)
            else:
                raiz.derecha = self._insertar(raiz.derecha, valor)
        return raiz

    def recorrer_en_orden(self,anios):
        lista = []
        lista = self._recorrer_en_orden(self.raiz,anios,lista)
        try:
            with open('Proyecto_por_fecha.txt', "w") as archivo:
                for proyecto in lista:
                    archivo.write(proyecto.__str__())
                    archivo.write('\n')
        except Exception:
            pass
        print()

    def _recorrer_en_orden(self, raiz, anios, lista):
        if raiz:
            for anio in anios:
                if convertirfecha_datetime(raiz.valor.fecha_inicio).year == anio:
                    self._recorrer_en_orden(raiz.izquierda,anios,lista)
                    lista.append(raiz.valor)
                    self._recorrer_en_orden(raiz.derecha,anios,lista)
        return lista
    
    def printear(self):
        self._printear(self.raiz)
    print()

    def _printear(self, raiz):
        if raiz:
            self._printear(raiz.izquierda)
            print(raiz.valor, end=' ')
            self._printear(raiz.derecha)
        
            
            
            

# if __name__=='__main__':
#     roble=Arbol()
#     nodo=Nodo('2002/12/23')
#     roble.agregarNodo(nodo)
#     roble.inorder()
    