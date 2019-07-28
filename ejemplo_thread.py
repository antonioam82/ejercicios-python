import threading

#FUNCIÓN A EJECUTAR
def cuenta(n, name):
    count=n
    while count<10:
        print("")
        print(count)
        count+=1

#CREAMOS PROCESOS A EJECUTAR EN PARALELO.        
t = threading.Thread(target = cuenta, args =(1, 'thread1') )
t2 = threading.Thread(target = cuenta, args =(2, 'thread2') )
t3 = threading.Thread(target = cuenta, args =(3, 'thread3') )

#INICIAMOS PROCESOS.
t.start()
t2.start()
t3.start()
