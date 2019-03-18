#IMPORTAMOS "deque".
from collections import deque

class Cola(object):
    def __init__(self):
        self.items=deque()
        
    #AÑADE ELEMENTOS A LA COLA POR LA IZQUIERDA
    def encolar(self,x): 
        self.items.appendleft(x)
        
    #MUESTRA COLA
    def muestra_cola(self):
        print(self.items)
        
    #VERIFICA SI LA COLA ESTA VACIA
    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False
        
    #DEVUELVE ELEMENTO DE LA COLA POR LA DERECHA
    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()
