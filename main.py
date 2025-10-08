from config import *
from utils.clases import *
import tkinter as tk
from tkinter import messagebox

Bibliotec = Biblioteca()

#------------------ Ventana ------------------#
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Biblioteca")
ventana.geometry("400x700")
ventana.resizable(0,0)
#---------------------------------------------#

#------------------ Boton "agregar_libros" ------------------#
def a_l(): #agrgar_libros()
    subventana = tk.Toplevel(ventana)
    subventana.title("Agregar Libros")
    subventana.geometry("400x400")

#---------------------------------------------#
    etiqueta_nombre = tk.Label(subventana, text = "Ingresa El Nombre: ")
    etiqueta_nombre.place(relx=0.5, rely=0.1, anchor= "center")
    entrada_nombre = tk.Entry(subventana)
    entrada_nombre.place(relx=0.5, rely=0.15, anchor= "center")
#---------------------------------------------#

#---------------------------------------------#
    etiqueta_autor = tk.Label(subventana, text = "Ingresa El Autor: ")
    etiqueta_autor.place(relx=0.5, rely=0.3, anchor= "center")
    entrada_autor = tk.Entry(subventana)
    entrada_autor.place(relx=0.5, rely=0.35, anchor= "center")
#---------------------------------------------#

#---------------------------------------------# 
    etiqueta_genero = tk.Label(subventana, text = "Ingresa El Genero: ")
    etiqueta_genero.place(relx=0.5, rely=0.5, anchor= "center")
    entrada_genero = tk.Entry(subventana)
    entrada_genero.place(relx=0.5, rely=0.55, anchor= "center")
#---------------------------------------------#

#---------------------------------------------#
    etiqueta_año = tk.Label(subventana, text = "Ingresa El Año De Publicacion: ")
    etiqueta_año.place(relx=0.5, rely=0.7, anchor= "center")
    entrada_año = tk.Entry(subventana)
    entrada_año.place(relx=0.5, rely=0.75, anchor= "center")
#---------------------------------------------#
    def g(): #guadar
        nombre = entrada_nombre.get()
        genero = entrada_genero.get()
        autor = entrada_autor.get()
        try:
            año = int(entrada_año.get())
        except ValueError:
            messagebox.showwarning("ValueError", "El valor debe ser númerico")
        
    
        libro = Libro(nombre, genero, autor, año)
        Bibliotec.agregarLibro(libro)

        messagebox.showwarning("Exito", "El libro ha sido guardado")


    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= g)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")


boton = tk.Button(ventana, text= ("Agregar Libros"), width= 30, height= 5, command = a_l)
boton.place(relx=0.5, rely=0.1, anchor= "center")
#----------------------------------------------------#

#------------------ Boton "ver_libros" ------------------#
def v_l(): #ver_libros()
    subventana = tk.Toplevel(ventana)
    subventana.title("Ver Libros")
    subventana.geometry("400x400")

    titulodispo = Bibliotec.titulodispo()
    print(titulodispo)
    listbox = tk.Listbox(subventana)
    listbox.insert(0, *titulodispo)
    listbox.place(relx = 0.5, rely = 0.5, anchor= "center")
boton = tk.Button(ventana, text= ("Ver Libros"), width= 30, height= 5, command = v_l)
boton.place(relx=0.5, rely=0.3, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "buscar_libros" ------------------#
def b_l(): #buscar_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Agregar Notas")
    subventana.geometry("400x300")

    def g ():
        titulo = entrada_n.get()
        name,autor,genero,año = Bibliotec.buscarLibro(titulo)

        etiqueta_n = tk.Label(subventana, text = "Nombre:", width=10, font = ("Arial", 12))
        etiqueta_n.place(relx=0.5, rely=0.3, anchor= "center")

        etiqueta_a = tk.Label(subventana, text = "Autor:", width=10, font = ("Arial", 12))
        etiqueta_a.place(relx=0.5, rely=0.45, anchor= "center")

        etiqueta_g = tk.Label(subventana, text = "Genero:", width=10, font = ("Arial", 12))
        etiqueta_g.place(relx=0.5, rely=0.6, anchor= "center")

        etiqueta_ñ = tk.Label(subventana, text = "Año:", width=10, font = ("Arial", 12))
        etiqueta_ñ.place(relx=0.5, rely=0.75, anchor= "center")



        etiqueta_n = tk.Label(subventana, text = name, width=10)
        etiqueta_n.place(relx=0.5, rely=0.36, anchor= "center")

        etiqueta_a = tk.Label(subventana, text = autor, width=10)
        etiqueta_a.place(relx=0.5, rely=0.51, anchor= "center")

        etiqueta_g = tk.Label(subventana, text = genero, width=10)
        etiqueta_g.place(relx=0.5, rely=0.66, anchor= "center")

        etiqueta_ñ = tk.Label(subventana, text = año, width=10)
        etiqueta_ñ.place(relx=0.5, rely=0.81, anchor= "center")

    etiqueta_n = tk.Label(subventana, text = "Nombre del libro")
    etiqueta_n.place(relx=0.5, rely=0.05, anchor= "center")
    entrada_n = tk.Entry(subventana)
    entrada_n.place(relx=0.5, rely=0.1, anchor= "center")
    boton_n = tk.Button(subventana, text= "Buscar", command= g)
    boton_n.place(relx= 0.5, rely= 0.2, anchor= "center")


boton = tk.Button(ventana, text= ("Buscar Libros"), width= 30, height= 5, command = b_l)
boton.place(relx=0.5, rely=0.5, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "prestar_libros" ------------------#
def p_l(): #prestar_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Prestar Libro")
    subventana.geometry("400x400")
#---------------------------------------------# 
    etiqueta_t = tk.Label(subventana, text = "Ingresa El Titulo: ")
    etiqueta_t.place(relx=0.5, rely=0.4, anchor= "center")
    entrada_t = tk.Entry(subventana)
    entrada_t.place(relx=0.5, rely=0.45, anchor= "center")
#---------------------------------------------# 
    def p(): #prestar
        t = entrada_t.get() #titulo
        Bibliotec.prestarPorTitulo(t)

    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= p)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")

boton = tk.Button(ventana, text= ("Prestar Libros"), width= 30, height= 5, command = p_l)
boton.place(relx=0.5, rely=0.7, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "devoler_libros" ------------------#
def d_l(): #devolver_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Devolver Libro")
    subventana.geometry("400x400")
#---------------------------------------------# 
    etiqueta_t = tk.Label(subventana, text = "Ingresa El Titulo: ")
    etiqueta_t.place(relx=0.5, rely=0.4, anchor= "center")
    entrada_t = tk.Entry(subventana)
    entrada_t.place(relx=0.5, rely=0.45, anchor= "center")
#---------------------------------------------# 
    def d(): #devolver
        t = entrada_t.get() #titulo
        Bibliotec.devolverPorTitulo(t)
        print("libro devolvido")

    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= d)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")

boton = tk.Button(ventana, text= ("Devolver Libros"), width= 30, height= 5, command = d_l)
boton.place(relx=0.5, rely=0.9, anchor= "center")

#----------------------------------------------------#

ventana.mainloop() #Permite hacer loop infinito
