#IMPORTAMOS MODULO "timeit".
import timeit

#CREAMOS LA CADENA "dias".
dias=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

#UNIMOS LOS ELEMENTOS SIN ESPACIOS:

#MEDINATE CICLO "for".
def cadena_sim(dias):
  cadena_final = ''
  for i in dias:
    cadena_final += i
  return cadena_final

 #MEDIANTE FORMATO.
def cadena_formato(dias):
  cadena_final = "%s%s%s%s%s%s%s" % (dias[0], dias[1],
  dias[2], dias[3],
  dias[4], dias[5],
  dias[6])
  return cadena_final

#MEDIANTE FUNCIÓN ".join". 
def join_cadena(dias):
  return ('').join(dias)

#VISUALIZAMOS TIEMPO DE EJECUCIÓN (EN MILESIMAS DE SEGUNDO) PARA CADA FUNCIÓN.
print('join_cadena() Tiempo de ejecución: ' + str(timeit.timeit('join_cadena(dias)', setup='from __main__ import join_cadena, dias')))
print('cadena_formato() Tiempo de ejecución: '+ str(timeit.timeit('cadena_formato(dias)', setup='from __main__ import cadena_formato, dias')))
print('cadena_sim() Tiempo de ejecución: ' + str(timeit.timeit('cadena_sim(dias)', setup='from __main__ import cadena_sim, dias')))

