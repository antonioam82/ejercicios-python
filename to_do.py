import tkinter as tk
import json

def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        tareas.append(tarea)
        guardar_tareas()
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    tarea_seleccionada = lista_tareas.curselection()
    if tarea_seleccionada:
        indice = tarea_seleccionada[0]
        tarea_eliminada = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        tareas.remove(tarea_eliminada)
        guardar_tareas()

root = tk.Tk()
root.title("Lista de Tareas")
root.configure(bg="light blue")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tareas = cargar_tareas()

lista_tareas = tk.Listbox(frame, width=40, height=10)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)
lista_tareas.configure(selectmode='multiple')

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas.yview)

for tarea in tareas:
    lista_tareas.insert(tk.END, tarea)

entrada_tarea = tk.Entry(root, width=30)
entrada_tarea.pack()

btn_agregar = tk.Button(root, text="Agregar tarea", width=15, bg="gray88", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar tarea", width=15, bg="gray88", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

root.mainloop()
