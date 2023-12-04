class Nodo ():
    def __init__(self,valor=None):
        self.valor=valor
        self.derecha=None
        self.izquierda=None
    
    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.derecho==None:raiz.derecho=nodo
            else:
                raiz.derecho.agregarnodos(nodo)
        elif raiz.dato>nodo.dato:
            if raiz.izquierdo==None:
                raiz.izquierdo=nodo
            else:raiz.izquierdo.agregarnodos(nodo)