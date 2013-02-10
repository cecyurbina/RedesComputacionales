#!/usr/bin/python
#Programa para dibujar tipo paint

from  Tkinter import *
trace = 1
class Interfaz:
    """
    """
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.linea = Button(self.frame, text="linea",bg="white",
                            command=lambda:self.seleccion("linea"))
        self.linea.grid(row=1, column=0,padx=15, pady=7)
        self.circulo = Button(self.frame, text="circulo", bg="white",
                              command=lambda:self.seleccion("circulo"))
        self.circulo.grid(row=2, column=0,padx=15, pady=7)
        self.rectangulo = Button(self.frame, text="rectangulo",
                                 bg="white", command=lambda:self.seleccion("rectangulo"))
        self.rectangulo.grid(row=3, column=0,padx=15, pady=7)
        canvas = Canvas(self.frame, width=700, height=500, bd=1,
                        highlightcolor="black", relief='solid',
                        background="white")
        canvas.grid(row=1, column=1, rowspan=4, columnspan=7,
                    sticky=W+E+N+S, padx=5, pady=5)
        canvas.bind('<ButtonPress-1>', self.click)
        canvas.bind('<B1-Motion>', self.mueve)
        self.canvas = canvas
        self.borrar = Button(self.frame, text="borrar", bg="white",
                             command=self.borrar)
        self.borrar.grid(row=4, column=0,padx=15, pady=7)
        self.grosor = 1
        self.color = "black"
        self.dibujo = None
        self.figura = "linea"
        self.mas_gruesa = Button(self.frame, text="+", bg="white",
                                 command=lambda:self.conf_linea("+"))
        self.mas_gruesa.grid(row=0, column=1,padx=15, pady=7)
        self.menos_gruesa = Button(self.frame, text="-", bg="white",
                                   command=lambda:self.conf_linea("-"))
        self.menos_gruesa.grid(row=0, column=2,padx=15, pady=7)
        self.rojo = Button(self.frame, bg="red",
                           command=lambda:self.cambiar_color("red"))
        self.rojo.grid(row=0, column=3,padx=15, pady=7)
        self.verde = Button(self.frame, bg="green",
                            command=lambda:self.cambiar_color("green"))
        self.verde.grid(row=0, column=4,padx=15, pady=7)
        self.azul = Button(self.frame, bg="blue",
                           command=lambda:self.cambiar_color("blue"))
        self.azul.grid(row=0, column=5,padx=15, pady=7)
        self.yellow = Button(self.frame, bg="yellow",
                             command=lambda:self.cambiar_color("yellow"))
        self.yellow.grid(row=0, column=6,padx=15, pady=7)
        self.black = Button(self.frame, bg="black",
                            command=lambda:self.cambiar_color("black"))
        self.black.grid(row=0, column=7,padx=15, pady=7)
        
    def click(self, event):
        self.inicio = event
        self.dibujo = None

    def conf_linea(self, dire):
        if dire == "+":
            self.grosor = self.grosor + 1
        else:
            if self.grosor == 1:
                return
            self.grosor = self.grosor - 1            

    def cambiar_color(self, color):
        self.color = color

    def borrar(self):
        ALL =  self.canvas.find_all()
        for fig in ALL:
            self.canvas.delete(fig)
        
    def seleccion(self, objeto):
        self.figura = objeto

    def mueve(self, event):
        canvas = event.widget
        if self.dibujo:
            canvas.delete(self.dibujo)
        if self.figura == "linea":
            id_objeto = canvas.create_line(self.inicio.x, self.inicio.y, event.x, event.y, width=str(self.grosor), fill=self.color)
        if self.figura == "circulo":
            id_objeto = canvas.create_oval(self.inicio.x, self.inicio.y, event.x, event.y, width=str(self.grosor), outline=self.color)
        if self.figura == "rectangulo":
            id_objeto = canvas.create_rectangle(self.inicio.x, self.inicio.y, event.x, event.y, width=str(self.grosor), outline=self.color)
        self.dibujo = id_objeto
            

def main():
    """
    """
    root = Tk()
    App = Interfaz(root)
    root.title("Dibuja")
    root.mainloop()

if __name__ == "__main__":
    main()

