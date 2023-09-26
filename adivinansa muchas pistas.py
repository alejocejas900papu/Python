import tkinter as tk
from tkinter import messagebox

class AdivinanzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinanza")

        self.label_instrucciones = tk.Label(root, text="ADIVINANZA 1.")
        self.label_instrucciones.pack()

        adivinanza = "rojo por dentro, verde por fuera"
        self.label_adivinanza = tk.Label(root, text=adivinanza)
        self.label_adivinanza.pack()

        self.label_respuesta = tk.Label(root, text="Adivina la respuesta:")
        self.label_respuesta.pack()

        self.entry_respuesta = tk.Entry(root)
        self.entry_respuesta.pack()

        self.boton_verificar = tk.Button(root, text="Verificar", command=self.verificar_respuesta)
        self.boton_verificar.pack()

        self.boton_pista = tk.Button(root, text="Pista", command=self.mostrar_pista)
        self.boton_pista.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

        # Lista de pistas para la adivinanza
        self.pistas = [
            "Es una fruta",
            "tiene cascara fea ",
            "Es jugosa y se come fresca",
        ]
        self.pista_actual = 0

    def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get().lower()
        if respuesta == "sandia":
            resultado = "¡Correcto! ¡Felicitaciones!"
            emoji = "\U0001F600"
        else:
            resultado = "Incorrecto. La respuesta es 'sandia'."
            emoji = "\U0001F92A"
        self.label_resultado.config(text=resultado + f" {emoji*3}")

    def mostrar_pista(self):
        if self.pista_actual < len(self.pistas):
            pista = self.pistas[self.pista_actual]
            messagebox.showinfo("Pista", pista)
            self.pista_actual += 1
        else:
            messagebox.showinfo("Pista", "No tenes mas pistas")

# Crear ventana principal
root = tk.Tk()
app = AdivinanzaApp(root)
root.mainloop()