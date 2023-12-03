from Proyecto import *
from FuncionesFinal import *
from Nodo import *

class Arbolito:
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
            
            
            
            
class Arbol():
    def __init__(self,nodo=None):
        self.raiz=nodo
    # agregar al arbol
    def agregarnodo(self,nodo):
        if self.raiz==None:
            self.raiz=nodo
        else:
            raiz=self.raiz
            #NodoArbol.agregarnodos(raiz,nodo)
            raiz.agregarnodos(nodo)
    # Mostrar el arbol en preorden
    def preorder(self,nodo):
        if nodo:
            print(self,nodo.dato)
            self.preorder(nodo.izquierdo)
            self.preorder(nodo.derecho)
    # Mostrar el arbol en inorden
    def inorder(self,nodo):
        if(nodo):
            self.inorder(nodo.izquierdo)
            print(nodo.dato)
            self.inorder(nodo.derecho)
    # Mostrar ecuacion en postorden
    def posorden(self,nodo):
        if nodo:
            self.posorden(nodo.izquierdo)
            self.posorden(nodo.derecho)
            print(nodo.dato)

if __name__=='__main__':
    roble=Arbol
    roble.insertar('2002/12/23')
    roble.recorrer_inorden()
    