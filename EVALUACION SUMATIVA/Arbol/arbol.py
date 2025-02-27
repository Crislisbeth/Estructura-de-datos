import re


class Nodo:
    def __init__(self, valor):
        self.valor = valor  
        self.izquierda = None
        self.derecha = None


def infijo_a_postfijo(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    salida = []
    pila = []
    
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expresion)
    
    for token in tokens:
        if token.isnumeric():
            salida.append(token)  
        elif token in precedencia:
            while pila and pila[-1] != "(" and precedencia[token] <= precedencia.get(pila[-1], 0):
                salida.append(pila.pop())  
            pila.append(token)
        elif token == "(":
            pila.append(token)  
        elif token == ")":
            while pila and pila[-1] != "(":
                salida.append(pila.pop())  
            pila.pop() 
    
    while pila:
        salida.append(pila.pop())  

    return salida  
def construir_arbol(expresion_postfija):
    pila = []
    
    for token in expresion_postfija:
        if token.isnumeric():
            pila.append(Nodo(float(token)))  
        else:
            nodo = Nodo(token)  
            nodo.derecha = pila.pop()  
            pila.append(nodo)  
    
    return pila[0]  
def evaluar_arbol(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        return nodo.valor  

    izquierda = evaluar_arbol(nodo.izquierda)
    derecha = evaluar_arbol(nodo.derecha)

    if nodo.valor == "+":
        return izquierda + derecha
    elif nodo.valor == "-":
        return izquierda - derecha
    elif nodo.valor == "*":
        return izquierda * derecha
    elif nodo.valor == "/":
        return izquierda / derecha

# Prueba del código
expresion = "3 + 5 * (2 - 8)"
postfija = infijo_a_postfijo(expresion)  
arbol = construir_arbol(postfija)  
resultado = evaluar_arbol(arbol)  

print("Expresion:", expresion)
print("Notacion postfija:", postfija)
print("Resultado:", resultado)
