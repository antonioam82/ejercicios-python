import queue
import threading
import time

# Crear una cola
tareas = queue.Queue()

# Función para que los trabajadores procesen la cola
def procesar_tarea():
    while not tareas.empty():
        tarea = tareas.get()
        print(f"Procesando {tarea}")
        time.sleep(1)  # Simula el tiempo de procesamiento
        tareas.task_done()

# Agregar tareas a la cola
for i in range(5):
    tareas.put(f"Tarea {i+1}")

start_time = time.time()

# Crear y lanzar múltiples hilos
hilos = []
for _ in range(3):  # 3 hilos procesando
    hilo = threading.Thread(target=procesar_tarea)
    hilo.start()
    hilos.append(hilo)

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

end_time = time.time()
execution_time = end_time - start_time

print(f"Todas las tareas han sido procesadas en {execution_time:.2f} segundos.")
