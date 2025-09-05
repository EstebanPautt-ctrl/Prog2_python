import tkinter as tk
from tkinter import messagebox

def guardar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    genero = var_genero.get()
    correo = entry_correo.get()
    edad = entry_edad.get()
    
    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nGénero: {genero}\nCorreo: {correo}\nEdad: {edad}"
    
    messagebox.showinfo("Registro Guardado", mensaje)

def reset():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_genero.set("")

ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x300")

label_nombre = tk.Label(ventana, text="Nombres:")
label_nombre.place(x=50, y=30)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.place(x=150, y=30)

label_apellido = tk.Label(ventana, text="Apellidos:")
label_apellido.place(x=50, y=70)
entry_apellido = tk.Entry(ventana, width=30)
entry_apellido.place(x=150, y=70)

label_genero = tk.Label(ventana, text="Género:")
label_genero.place(x=50, y=110)
var_genero = tk.StringVar()
radio_m = tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value="Masculino")
radio_m.place(x=150, y=110)
radio_f = tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value="Femenino")
radio_f.place(x=250, y=110)

label_correo = tk.Label(ventana, text="Correo:")
label_correo.place(x=50, y=150)
entry_correo = tk.Entry(ventana, width=30)
entry_correo.place(x=150, y=150)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.place(x=50, y=190)
entry_edad = tk.Entry(ventana, width=30)
entry_edad.place(x=150, y=190)

btn_guardar = tk.Button(ventana, text="Guardar", command=guardar)
btn_guardar.place(x=150, y=230, width=80)

btn_reset = tk.Button(ventana, text="Reset", command=reset)
btn_reset.place(x=250, y=230, width=80)

ventana.mainloop()
