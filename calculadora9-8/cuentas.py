import random
import tkinter

#suma
def suma_random():
    a = random.randrange(0,500)
    b = random.randrange(-500,500)
    c = a+b
    d = str(a)
    e = str (b)
    f = str(c)
    def resultado():
        etiquetaResultado = tkinter.Label(ventana, font="Arial 20", text= f)
        etiquetaResultado.pack()
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    etiquetaA = tkinter.Label(ventana, font="Arial 20", text= d)
    etiquetaB = tkinter.Label(ventana, font="Arial 20", text= e)
    #etiquetaC = tkinter.Label(ventana, font="Arial 20", text="+")
    etiquetaA.pack()
    #etiquetaC.pack()
    etiquetaB.pack()
    botonResultado = tkinter.Button(ventana, command = resultado,font="Arial 20", text="ver resultado", bg="aquamarine2")
    botonResultado.pack()

    ventana.mainloop()

#resta
def resta_random():
    a = random.randrange(1,500)
    b = random.randrange(-500,0)
    c = a+b
    d = str(a)
    e = str (b)
    f = str(c)
    def resultado():
        etiquetaResultado = tkinter.Label(ventana, font="Arial 20", text= f)
        etiquetaResultado.pack()
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    etiquetaA = tkinter.Label(ventana, font="Arial 20", text= d)
    etiquetaB = tkinter.Label(ventana, font="Arial 20", text= e)
    #etiquetaC = tkinter.Label(ventana, font="Arial 20", text="-")
    etiquetaA.pack()
    #etiquetaC.pack()
    etiquetaB.pack()
    botonResultado = tkinter.Button(ventana, command = resultado,font="Arial 20", text="ver resultado", bg="aquamarine2")
    botonResultado.pack()

    ventana.mainloop()


#multiplicar
def multiplicacion_random():
    a = random.randrange(-30,30)
    b = random.randrange(-12,12)
    c = a*b
    d = str(a)
    e = str (b)
    f = str(c)
    def resultado():
        etiquetaResultado = tkinter.Label(ventana, font="Arial 20", text= f)
        etiquetaResultado.pack()
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    etiquetaA = tkinter.Label(ventana, font="Arial 20", text= d)
    etiquetaB = tkinter.Label(ventana, font="Arial 20", text= e)
    #etiquetaC = tkinter.Label(ventana, font="Arial 20", text="+")
    etiquetaA.pack()
    #etiquetaC.pack()
    etiquetaB.pack()
    botonResultado = tkinter.Button(ventana, command = resultado,font="Arial 20", text="ver resultado", bg="aquamarine2")
    botonResultado.pack()

    ventana.mainloop()


#dividir
def division_random():
    a = random.randrange(50,100)
    b = random.randrange(1,10)
    c = a/b
    d = str(a)
    e = str (b)
    f = str(c)

    def resultado():
        etiquetaResultado = tkinter.Label(ventana, font="Arial 20", text= f)
        etiquetaResultado.pack()
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    etiquetaA = tkinter.Label(ventana, font="Arial 20", text= d)
    etiquetaB = tkinter.Label(ventana, font="Arial 20", text= e)
    #etiquetaC = tkinter.Label(ventana, font="Arial 20", text="+")
    etiquetaA.pack()
    #etiquetaC.pack()
    etiquetaB.pack()
    botonResultado = tkinter.Button(ventana, command = resultado,font="Arial 20", text="ver resultado", bg="aquamarine2")
    botonResultado.pack()

    ventana.mainloop()


#ventana principal
ventana = tkinter.Tk()
ventana.geometry("400x600")

etiqueta = tkinter.Label(ventana, font = "Arial 30", text="RECALCULANDO", bg = "CadetBlue2" )
etiqueta.pack()
botonSuma = tkinter.Button(ventana, command = suma_random, font="Arial 20" , text="Sumar", padx=70, pady=30, bg = "medium turquoise")
botonSuma.pack()
botonResta = tkinter.Button(ventana, command = resta_random, font="Arial 20" , text="Restar", padx=70, pady=30, bg = "aquamarine2")
botonResta.pack()
botonMultiplica = tkinter.Button(ventana, command = multiplicacion_random, font="Arial 20" , text="Multiplicar", padx=50, pady=30, bg = "medium turquoise")
botonMultiplica.pack()
botonDivision = tkinter.Button(ventana, command = division_random, font="Arial 20" , text="Dividir", padx=74, pady=30, bg = "aquamarine2")
botonDivision.pack()


ventana.mainloop()




