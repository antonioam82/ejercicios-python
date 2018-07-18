import time
#CREAMOS DECORADOR
def decorador(funci):
    def div_text(*args, **kwargs):
        t1=time.time()
        print("Efectuando división")
        resultado=funci(*args, **kwargs)
        t2=time.time()
        print('La función tardó {0} segundos en ejecutarse'.format(t2-t1))
        return resultado
    return div_text

#APLICAMOS DECORADOR A UNA FUNCIÓN CON ARGUMENTOS
@decorador
def division(num, num2):
    return num/num2

#VISUALIZAMOS RESULTADO
resultado=division(12, 7)
print(resultado)
