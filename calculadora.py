from tkinter import *
from tkinter import ttk
import math


#las funciones de la calculadora pero con el teclado
def tecladoNumerico(event):
    tecla = event.char
    if tecla >= '0' and tecla <='9' or tecla == '(' or tecla ==')' or tecla =='.':
        #seteo el valor que tenía + el valor que botoneo como string
        entrada2.set(entrada2.get()+ tecla)
    if tecla == '+' or tecla == '-' or tecla == '/' or tecla == '*':
        if tecla == '+':
            entrada1.set(entrada2.get()+'+')
        elif tecla =='-':
            entrada1.set(entrada2.get()+'-')
        elif tecla == '/':
            entrada1.set(entrada2.get()+'/')
        elif tecla =='*':
            entrada1.set(entrada2.get()+'*')
        entrada2.set('')
    if tecla == '=' or tecla == chr(13):
        entrada1.set(entrada1.get() + entrada2.get())
        #eval toma todo lo que tenga sentido matemático y lo calcula
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
    if tecla == 'c':
        entrada1.set('')
        entrada2.set('')
    if tecla =='b':
        entrada2.set(entrada2.get()[0:len(entrada2.get())-1])
#lógica
def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def ingresarValores(tecla):
    if tecla >= '0' and tecla <='9' or tecla == '(' or tecla ==')' or tecla =='.':
        #seteo el valor que tenía + el valor que botoneo como string
        entrada2.set(entrada2.get()+ tecla)
    if tecla == '+' or tecla == '-' or tecla == '/' or tecla == 'x':
        if tecla == '+':
            entrada1.set(entrada2.get()+'+')
        elif tecla =='-':
            entrada1.set(entrada2.get()+'-')
        elif tecla == '/':
            entrada1.set(entrada2.get()+'/')
        elif tecla =='x':
            entrada1.set(entrada2.get()+'*')
        entrada2.set('')
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        #eval toma todo lo que tenga sentido matemático y lo calcula
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
    if tecla == 'c':
        entrada1.set('')
        entrada2.set('')
    if tecla =='b':
        entrada2.set(entrada2.get()[0:len(entrada2.get())-1])
        

#ventana base
root = Tk()
#titulo de la ventana
root.title("Mi primer calculadora")
#defino medidas
root.geometry("+500+80")
#anclo los objetos al medios
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#estilo 
estilo = ttk.Style()
#estilo que voy a usar 
estilo.theme_use('clam')
#doy nombre al estilo usado para TFrame y color de fondo
estilo.configure('mainFrame.TFrame', background="#00BFBF")


#inicio mi frame principal
mainFrame = ttk.Frame(root, style="mainFrame.TFrame")
#le digo donde empieza 0-0 con el sticky le digo donde anclarse
mainFrame.grid(column=0, row=0, sticky=(W, N, E, S))

#columna 0 tiene un peso de 1
mainFrame.columnconfigure(0, weight=1)  
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)
mainFrame.columnconfigure(3, weight=1)
#fila 0 tiene un peso de 1
mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)
mainFrame.rowconfigure(4, weight=1)
mainFrame.rowconfigure(5, weight=1)
mainFrame.rowconfigure(6, weight=1)
mainFrame.rowconfigure(7, weight=1)

#doy estilo a las etiquetas
estiloLabel1 = ttk.Style()
estiloLabel1.configure('label_entrada1.TLabel', font="arial 15", anchor = "e")
estiloLabel2 = ttk.Style()
estiloLabel2.configure('label_entrada2.TLabel', font="arial 30", anchor = "e")

#entrada de valor a calcular
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainFrame, textvariable = entrada1, style="label_entrada1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))
#segunda entrada de valor a calcular
entrada2 = StringVar()
label_entrada2 = ttk.Label(mainFrame, textvariable = entrada2, style='label_entrada2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S)) 

#estilo de los botones
estiloNumeros = ttk.Style()
estiloNumeros.configure('botonesStyle.TButton', font = 'arial 30', width=5, relief='flat', background='#FFFFFF')
estiloBotones = ttk.Style()
estiloBotones.configure('botones.TButton', font = 'arial 30', width=5, relief='flat', background='#CECECE'  )
#doy estilo cuando paso el mouse por arriba
estiloNumeros.map('botonesStyle.TButton', foreground=[('active', '#BFBF00')])
estiloBotones.map('botones.TButton', foreground=[('active', '#00BFBF')] )    

#defino botones 
button0 = ttk.Button(mainFrame, text="0", style='botonesStyle.TButton', command=lambda:ingresarValores('0'))
button1 = ttk.Button(mainFrame, text="1", style='botonesStyle.TButton', command=lambda:ingresarValores('1'))
button2 = ttk.Button(mainFrame, text="2", style='botonesStyle.TButton', command=lambda:ingresarValores('2'))
button3 = ttk.Button(mainFrame, text="3", style='botonesStyle.TButton', command=lambda:ingresarValores('3'))
button4 = ttk.Button(mainFrame, text="4", style='botonesStyle.TButton', command=lambda:ingresarValores('4'))
button5 = ttk.Button(mainFrame, text="5", style='botonesStyle.TButton', command=lambda:ingresarValores('5'))
button6 = ttk.Button(mainFrame, text="6", style='botonesStyle.TButton', command=lambda:ingresarValores('6'))
button7 = ttk.Button(mainFrame, text="7", style='botonesStyle.TButton', command=lambda:ingresarValores('7'))
button8 = ttk.Button(mainFrame, text="8", style='botonesStyle.TButton', command=lambda:ingresarValores('8'))
button9 = ttk.Button(mainFrame, text="9", style='botonesStyle.TButton', command=lambda:ingresarValores('9'))

botonBorrar = ttk.Button(mainFrame, text=chr(9003), style='botones.TButton', command=lambda:ingresarValores('b'))
botonBorrarTodo = ttk.Button(mainFrame, text="C", style='botones.TButton', command=lambda:ingresarValores('c'))
botonParentesisA = ttk.Button(mainFrame, text="(", style='botones.TButton', command=lambda:ingresarValores('('))
botonParentesisC = ttk.Button(mainFrame, text=")", style='botones.TButton', command=lambda:ingresarValores(')'))
botonPunto = ttk.Button(mainFrame, text=".", style='botones.TButton', command=lambda:ingresarValores('.'))
botonIgual = ttk.Button(mainFrame, text="=", style='botones.TButton', command=lambda:ingresarValores('='))

botonSuma = ttk.Button(mainFrame, text="+", style='botones.TButton', command=lambda:ingresarValores('+'))
botonResta = ttk.Button(mainFrame, text="-", style='botones.TButton', command=lambda:ingresarValores('-'))
botonMultiplica = ttk.Button(mainFrame, text="x", style='botones.TButton', command=lambda:ingresarValores('x'))
botonDivide = ttk.Button(mainFrame, text='/', style='botones.TButton', command=lambda:ingresarValores('/'))
botonRaiz = ttk.Button(mainFrame, text="√", style='botones.TButton', command=lambda:raizCuadrada())

#organizo los botones en pantalla
botonParentesisA.grid(column=0, row=2)
botonParentesisC.grid(column=1, row=2)
botonBorrarTodo.grid(column=2, row=2)
botonBorrar.grid(column=3, row=2)
button7.grid(column=0,row=3)
button8.grid(column=1,row=3)
button9.grid(column=2,row=3)
botonDivide.grid(column=3, row=3)
button4.grid(column=0,row=4)
button5.grid(column=1,row=4)
button6.grid(column=2,row=4)
botonMultiplica.grid(column=3,row=4)
button1.grid(column=0,row=5)
button2.grid(column=1,row=5)
button3.grid(column=2,row=5)
botonSuma.grid(column=3,row=5)
button0.grid(column=0, row=6, columnspan=2, sticky=(W, E))
botonPunto.grid(column=2, row=6)
botonResta.grid(column=3, row=6)
botonIgual.grid(column=0, row=7, columnspan=3, sticky=(W,E))
botonRaiz.grid(column=3, row=7)

#recorro cada elemento del mainFrame
for child in mainFrame.winfo_children():
    #le configuro a cada elemento un pady de 1 y el ipady es el paddy con respecto del número a el final de su caja (botón)
    child.grid_configure(ipady=10, padx=1, pady=1) 

root.bind('<Key>', tecladoNumerico )
root.mainloop()

