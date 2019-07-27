import threading
import time

def print_time(name, n):
    count = 0
    while count < 5:
        time.sleep(n)
        count+=1
        print("%s: %s" % ( name, time.ctime(time.time()) ))

try:
    t1 = threading.Thread(target=print_time, args=("Thread-1", 2, ) )
    t2 = threading.Thread(target=print_time, args=("Thread-2", 4, ) )

except:
    print("No se pudo ejecutar el thread")

t1.start()
t2.start()
