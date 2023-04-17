# Importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# GENERER VENTANA
root = Tk()
root.title("CRUD APP")
root.geometry("600x350")


miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()

def conexion_BBDD():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    
    try:
        miCursor.execute('''
            CREATE TABLE empleado (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            NOMBRE VARCHAR(50) NOT NULL,
            CARGO VARCHAR(50) NOT NULL,
            SALARIO INT NOT NULL)
            ''')
        messagebox.showinfo("CONEXION","Base de datos creada correctamente")
    except:
        messagebox.showinfo("CONEXION","Conexión exitosa con la base de datos")

def eliminarBBDD():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderán definitivamente, Desea continuar?", title="ADVERTENCIA"):
        miCursor.execute("DROP TABLE empleado")
    else:
        pass

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Esta seguro que desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mensaje():
    acerca='''
    Aplicacion CRUD
    Versión 1.0
    Tecnologia Python Tkinter
    '''

###################################### Metodos CRUD


def crear():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)", (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al crear el registro, verifique conexion co base de datos")
        pass
    limpiarCampos()
    mostrar()

def mostrar():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleados")
        for row in miCursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
    except:
        pass

############################################################## Tabla ####################################

tree = ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0,y=130)

root.mainloop()
