import queue
import time

# Crear una cola
tareas = queue.Queue()

# Agregar tareas a la cola
for i in range(5):
    tareas.put(f"Tarea {i+1}")

# Función para procesar tareas de manera secuencial (sin hilos)
def procesar_tarea_secuencial():
    while not tareas.empty():
        tarea = tareas.get()
        print(f"Procesando {tarea}")
        time.sleep(1)  # Simula el tiempo de procesamiento
        tareas.task_done()

# Medir el tiempo de ejecución
start_time = time.time()

# Procesar las tareas de manera secuencial
procesar_tarea_secuencial()

end_time = time.time()

# Calcular y mostrar el tiempo de ejecución total
execution_time = end_time - start_time
print(f"Todas las tareas han sido procesadas en {execution_time:.2f} segundos.")

