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
miNombre = StrinVar()
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
