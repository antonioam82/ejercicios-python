#IMPLEMENTACION DE UNA PILA EN PYTHON.

class Pila(object):
    
    def __init__(self):
        self.items=[]

    def apilar(self, dato): #REALIZA ACCIÓN DE APILAR
        self.items.append(dato)

    def desapilar(self): #SACA ELEMENTOS DE LA PILA
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()

    def esta_vacia(self): #VERIFICA SI LA PILA ESTÁ VACIA
        if len(self.items)==0:
            return True
        else:
            return False
        
    def ver_pila(self): #VER ELEMENTOS DE LA PILA
        print(self.items)
