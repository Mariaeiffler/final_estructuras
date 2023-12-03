class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierda = insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def recorrer_inorden(raiz):
    if raiz:
        recorrer_inorden(raiz.izquierda)
        print(raiz.valor, end=' ')
        recorrer_inorden(raiz.derecha)

# Crear un árbol binario de ejemplo
arbol = None
datos = [5, 3, 7, 2, 4, 6, 8]

for dato in datos:
    arbol = insertar(arbol, dato)

# Imprimir el recorrido inorden del árbol
print("Recorrido Inorden:")
recorrer_inorden(arbol)