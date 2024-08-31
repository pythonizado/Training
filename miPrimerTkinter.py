import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("Calculando")
ventana.geometry("600x450+350+150")
ventana.resizable(width=True, height=True)
label1 = tkinter.Label(ventana, text="ingresa un valor", bg="black", fg="white", font="arial 12")
label1.pack(pady=10)
e_texto = tkinter.Entry(ventana, font="arial 20")
e_texto.pack()
label_texto = tkinter.Label(ventana)

def mostrar_texto():
    label_texto.pack()
    global i

    if e_texto.get()=="":
        label_texto.configure(bg="red", fg="white")
        label_texto["text"] = "Vacío"
        messagebox.showwarning("error", "aun no escribiste nada")

    else:
        label_texto.configure(bg="green", fg="white")
        label_texto["text"]=e_texto.get()
        messagebox.showerror("bien", "vamos bien brother")
button1 = tkinter.Button(ventana, text="click", command = mostrar_texto)
button1.pack()






ventana.mainloop()
