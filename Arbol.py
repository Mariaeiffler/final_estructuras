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
        self._recorrer_en_orden(self.raiz,anios)
        print()

    def _recorrer_en_orden(self, raiz, anios):
        if raiz:
            for anio in anios:
                if convertirfecha_datetime(raiz.valor.fecha_inicio).year == anio:
                    self._recorrer_en_orden(raiz.izquierda)
                    print(raiz.valor, end='\n')
                    self._recorrer_en_orden(raiz.derecha)
            
            

if __name__=='__main__':
    roble=Arbol()
    nodo=Nodo('2002/12/23')
    roble.agregarNodo(nodo)
    roble.inorder()
    