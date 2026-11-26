# Actividad 6 - Interfaz grafica y archivos de texto (CRUD)
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import os
import tkinter as tk
from tkinter import ttk, messagebox

ARCHIVO = "contactos.txt"


class Contacto:

    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def convertir_linea(self):
        return self.nombre + "," + self.numero + "\n"


class ArchivoContactos:

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer(self):
        contactos = []
        if not os.path.exists(self.nombre_archivo):
            return contactos

        archivo = open(self.nombre_archivo, "r", encoding="utf-8")
        linea = archivo.readline()
        while linea != "":
            if linea.strip() != "":
                datos = linea.strip().split(",")
                contactos.append(Contacto(datos[0], datos[1]))
            linea = archivo.readline()
        archivo.close()
        return contactos

    def escribir(self, contactos):
        archivo = open(self.nombre_archivo, "w", encoding="utf-8")
        for contacto in contactos:
            archivo.write(contacto.convertir_linea())
        archivo.close()

    def buscar(self, nombre):
        for contacto in self.leer():
            if contacto.nombre == nombre:
                return contacto
        return None

    def crear(self, contacto):
        if self.buscar(contacto.nombre) is not None:
            return False
        archivo = open(self.nombre_archivo, "a", encoding="utf-8")
        archivo.write(contacto.convertir_linea())
        archivo.close()
        return True

    def actualizar(self, nombre, numero):
        contactos = self.leer()
        for contacto in contactos:
            if contacto.nombre == nombre:
                contacto.numero = numero
                self.escribir(contactos)
                return True
        return False

    def eliminar(self, nombre):
        contactos = self.leer()
        for contacto in contactos:
            if contacto.nombre == nombre:
                contactos.remove(contacto)
                self.escribir(contactos)
                return True
        return False


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Agenda de contactos")
        self.resizable(False, False)
        self.archivo = ArchivoContactos(ARCHIVO)

        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.campo_nombre = tk.Entry(self, width=26)
        self.campo_nombre.grid(row=0, column=1, columnspan=3, padx=10, pady=8)

        tk.Label(self, text="Número").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.campo_numero = tk.Entry(self, width=26)
        self.campo_numero.grid(row=1, column=1, columnspan=3, padx=10, pady=8)

        botones = [("Create", self.crear), ("Read", self.leer),
                   ("Update", self.actualizar), ("Delete", self.eliminar)]
        for i, (texto, accion) in enumerate(botones):
            tk.Button(self, text=texto, width=8, command=accion).grid(row=2, column=i,
                                                                      padx=6, pady=10)

        self.tabla = ttk.Treeview(self, columns=("nombre", "numero"), show="headings",
                                  height=8)
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("numero", text="Número")
        self.tabla.column("nombre", width=180)
        self.tabla.column("numero", width=140)
        self.tabla.grid(row=3, column=0, columnspan=4, padx=10, pady=(0, 5))
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.etiqueta_estado = tk.Label(self, text="Archivo: " + ARCHIVO)
        self.etiqueta_estado.grid(row=4, column=0, columnspan=4, padx=10, pady=(0, 10),
                                  sticky="w")

        self.mostrar_contactos()

    def mostrar_contactos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for contacto in self.archivo.leer():
            self.tabla.insert("", tk.END, values=(contacto.nombre, contacto.numero))

    def seleccionar(self, evento):
        seleccion = self.tabla.selection()
        if len(seleccion) == 0:
            return
        nombre, numero = self.tabla.item(seleccion[0], "values")
        self.campo_nombre.delete(0, tk.END)
        self.campo_nombre.insert(0, nombre)
        self.campo_numero.delete(0, tk.END)
        self.campo_numero.insert(0, numero)

    def crear(self):
        nombre = self.campo_nombre.get().strip()
        numero = self.campo_numero.get().strip()
        if nombre == "" or numero == "":
            messagebox.showerror("Error", "El nombre y el número no pueden estar vacíos.")
            return

        if self.archivo.crear(Contacto(nombre, numero)):
            self.etiqueta_estado.config(text="Contacto " + nombre + " agregado al archivo.")
            self.limpiar()
        else:
            messagebox.showerror("Error", "Ya existe un contacto con ese nombre.")
        self.mostrar_contactos()

    def leer(self):
        nombre = self.campo_nombre.get().strip()
        self.mostrar_contactos()

        if nombre == "":
            self.etiqueta_estado.config(text="Se leyeron " +
                                        str(len(self.archivo.leer())) + " contactos.")
            return

        contacto = self.archivo.buscar(nombre)
        if contacto is None:
            messagebox.showerror("Error", "No existe un contacto con ese nombre.")
            return

        self.campo_numero.delete(0, tk.END)
        self.campo_numero.insert(0, contacto.numero)
        self.etiqueta_estado.config(text="Contacto " + nombre + " encontrado.")

    def actualizar(self):
        nombre = self.campo_nombre.get().strip()
        numero = self.campo_numero.get().strip()
        if nombre == "" or numero == "":
            messagebox.showerror("Error", "El nombre y el número no pueden estar vacíos.")
            return

        if self.archivo.actualizar(nombre, numero):
            self.etiqueta_estado.config(text="Contacto " + nombre + " actualizado.")
            self.limpiar()
        else:
            messagebox.showerror("Error", "No existe un contacto con ese nombre.")
        self.mostrar_contactos()

    def eliminar(self):
        nombre = self.campo_nombre.get().strip()
        if nombre == "":
            messagebox.showerror("Error", "Escriba el nombre del contacto a eliminar.")
            return

        if self.archivo.eliminar(nombre):
            self.etiqueta_estado.config(text="Contacto " + nombre + " eliminado.")
            self.limpiar()
        else:
            messagebox.showerror("Error", "No existe un contacto con ese nombre.")
        self.mostrar_contactos()

    def limpiar(self):
        self.campo_nombre.delete(0, tk.END)
        self.campo_numero.delete(0, tk.END)


ventana = VentanaPrincipal()
ventana.mainloop()
