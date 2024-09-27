import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random


def cargar_imagenes_aleatorias(directorio, num_imagenes=10):
    archivos = os.listdir(directorio)
    imagenes = []

    for archivo in archivos:
        if '.png' in archivo:
            imagenes.append(archivo)

    imagenes_seleccionadas = random.sample(imagenes, num_imagenes)
    return imagenes_seleccionadas


def comprobar_respuesta():
    global indice_imagen, puntuacion

    respuesta = entrada.get().lower()
    nombre_imagen = imagenes[indice_imagen].split('.')[0].lower()

    if respuesta == nombre_imagen:
        puntuacion += 1

    indice_imagen += 1
    if indice_imagen < len(imagenes):
        mostrar_imagen(imagenes[indice_imagen])
    else:
        mostrar_calificacion()


def mostrar_imagen(nombre_imagen):
    ruta_completa = directorio_imagenes  + nombre_imagen
    imagen = Image.open(ruta_completa)
    imagen = imagen.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk
    entrada.delete(0, tk.END)


def mostrar_calificacion():
    if puntuacion == 10:
        calificacion = "Sobresaliente"
    elif puntuacion >= 8:
        calificacion = "Notable"
    elif puntuacion == 6:
        calificacion = "Bien"
    elif puntuacion == 5:
        calificacion = "Suficiente"
    else:
        calificacion = "Suspenso"

    messagebox.showinfo("Calificación Final", f"Puntuación: {puntuacion}/10\nCalificación: {calificacion}")
    ventana.quit()




ventana = tk.Tk()
ventana.title("Hiragana")

directorio_imagenes = "/home/simon/Escritorio/hiragana/"

imagenes = cargar_imagenes_aleatorias(directorio_imagenes)

puntuacion = 0
indice_imagen = 0

label_imagen = tk.Label(ventana)
label_imagen.pack(padx=10, pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(padx=10, pady=10)

boton_comprobar = tk.Button(ventana, text="Comprobar", command=comprobar_respuesta)
boton_comprobar.pack(padx=10, pady=10)

mostrar_imagen(imagenes[indice_imagen])

ventana.mainloop()
