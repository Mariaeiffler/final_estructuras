from Proyecto import *
from FuncionesFinal import *
from Nodo import *

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, raiz, valor):
        if raiz is None:
            return Nodo(valor)
        else:
            if convertirfecha_datetime(valor.fecha_inicio) < raiz.convertirfecha_datetime(valor.fecha_inicio):
                raiz.izquierda = self._insertar(raiz.izquierda, valor)
            else:
                raiz.derecha = self._insertar(raiz.derecha, valor)
        return raiz

    def recorrer_inorden(self):
        self._recorrer_inorden(self.raiz)
        print()

    def _recorrer_inorden(self, raiz):
        if raiz:
            self._recorrer_inorden(raiz.izquierda)
            print(raiz.valor, end=' ')
            self._recorrer_inorden(raiz.derecha)

if __name__=='__main__':
    roble=Arbol
    roble.insertar('2002/12/23')
    roble.recorrer_inorden()
    