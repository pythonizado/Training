from tkinter import *

#creo una ventana principal
ventana = Tk()
ventana.geometry("500x500")


#funcion para contar digitos y letras devuelve una dupla
def letrasNumeros(textito: StringVar, caracter: StringVar):
    digitos = 0
    letras = 0
    arroba = 0
    caracteres = 0
    print(f'el textito es: {textito}')

    for i in textito:
        if i == caracter:
            caracteres +=1
        if i =='@':
            arroba +=1
        if i.isdigit():  
            digitos+=1
        elif i.isalpha():
            letras+=1
        else:
            pass
    
    print(f'los numeros son: {digitos}, las letras son: {letras}, las arrobas son: {arroba}, el caracter buscado suma: {caracteres}')    
    
    #salida de digitos
    label_numeros = Label(ventana, font='Arial20', text='la cantidad de números es: ')
    label_numeros.pack()
    outputDigitos = Label(ventana, font="Arial 20", text=digitos)
    outputDigitos.pack()

    #salida de letras
    label_letras = Label(ventana, font='Arial20', text='la cantidad de letras es: ')
    label_letras.pack()
    outputLetras = Label(ventana, font="Arial 20", text= letras)
    outputLetras.pack()

    #salida de arrobas
    label_arrobas = Label(ventana, font='Arial20', text='la cantidad de @ es: ')
    label_arrobas.pack()
    outputArrobas = Label(ventana, font="Arial 20", text= arroba)
    outputArrobas.pack()

    #salida de caracter deseado
    label_caracter = Label(ventana, font='Arial20', text='la cantidad del los caractes buscados es: ')
    label_caracter.pack()
    outputArrobas = Label(ventana, font="Arial 20", text= caracteres)
    outputArrobas.pack()

    return digitos,letras



#creo un label para decir lo que tienen que hacer
labelIngreso = Label(ventana, font="Arial 20", text= 'Ingrese su texto:')
labelIngreso.pack()


#defino una variable como un string
textoPantalla = StringVar()
caracter = StringVar()

#creo un label para atrapar el textVariable y guardarlo en la variable textoPantalla
cajita = Entry(ventana, cursor='Arrow', textvariable=textoPantalla)
cajita.pack()

#creo un label para decir que puede hacer
labelCaracter = Label(ventana, font="Arial 16", text= 'Ingrese un caracter a contar: ')
labelCaracter.pack()

cajitaCaracter = Entry(ventana, cursor='Arrow', textvariable=caracter)
cajitaCaracter.pack()


#obtengo el resultado para la fucnion letrasNumeros con el parametro textoPantalla y lambda me genera un evento
botonContar = Button(ventana, text='contar!!!', command= lambda:letrasNumeros(textoPantalla.get(), caracter.get()))
botonContar.pack()


#inicio la ventana
ventana.mainloop()

