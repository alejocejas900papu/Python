import tkinter as tk
from tkinter import Entry, Label, Button

def calcular_propina():
    total_cuenta = float(total_cuenta_entry.get())
    porcentaje_propina = float(porcentaje_propina_entry.get())
    
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina

    resultado_propina.config(text="Monto de la propina: ".format(propina))
    resultado_total.config(text="Total a pagar (con propina): ".format(total_a_pagar))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Propina")

# Etiqueta y entrada para el total de la cuenta
total_cuenta_label = Label(ventana, text="Ingrese el total de la cuenta:")
total_cuenta_label.pack()
total_cuenta_entry = Entry(ventana)
total_cuenta_entry.pack()

# Etiqueta y entrada para el porcentaje de propina
porcentaje_propina_label = Label(ventana, text="Ingrese el porcentaje de propina (%):")
porcentaje_propina_label.pack()
porcentaje_propina_entry = Entry(ventana)
porcentaje_propina_entry.pack()

# Botón para calcular la propina
calcular_button = Button(ventana, text="Calcular Propina", command=calcular_propina)
calcular_button.pack()

# Resultado de la propina y el total a pagar
resultado_propina = Label(ventana, text="")
resultado_propina.pack()
resultado_total = Label(ventana, text="")
resultado_total.pack()

ventana.mainloop()
