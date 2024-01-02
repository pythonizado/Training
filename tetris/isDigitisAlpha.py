from tkinter import *
import tkinter

#defino una variable como un string
textoPantalla = ''

#funcion para contar digitos y letras devuelve una dupla
def letrasNumeros(textoPantalla):
    digitos = 0
    letras = 0

    for i in textoPantalla:
        if i.isdigit():
            digitos+=1
        elif i.isalpha():
            letras+=1
        else:
            pass
    return digitos, letras

#creo una ventana principal
ventana = tkinter.Tk()
ventana.geometry("500x500")

#creo un label para decir lo que tienen que hacer
labelIngreso = tkinter.Label(ventana, font="Arial 20", text= 'Ingrese su texto:')
labelIngreso.pack()

#creo un label para atrapar el textVariable y guardarlo en la variable textoPantalla
box = Entry(ventana)
box.pack()
textoPantalla = box.get()



#obtengo el resultado para la fucnion letrasNumeros con el parametro textoPantalla
resultado = letrasNumeros(textoPantalla)
botonContar = tkinter.Button(ventana, text='contar!!!', command=letrasNumeros(textoPantalla))
botonContar.pack()

#print('cantidad de digitos: %1' % resultado[0])
#print('cantidad de letras : %1' % resultado[1])

#salida de digitos
outputDigitos = tkinter.Label(ventana, font="Arial 20", text= resultado[0])
outputDigitos.pack()

#salida de letras
outputLetras = tkinter.Label(ventana, font="Arial 20", text= resultado[1])
outputLetras.pack()

#imprimo en consola para ir haciendo pruebas unitarias
#print('cantidad de digitos: %1' % resultado[0])
#print('cantidad de letras : %1' % resultado[1])

#inicio la ventana
ventana.mainloop()