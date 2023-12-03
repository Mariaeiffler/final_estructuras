class Nodo ():
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None
    
    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.derecho==None:raiz.derecho=nodo
            else:
                raiz.derecho.agregarnodos(nodo)
        elif raiz.dato>nodo.dato:
            if raiz.izquierdo==None:
                raiz.izquierdo=nodo
            else:raiz.izquierdo.agregarnodos(nodo)