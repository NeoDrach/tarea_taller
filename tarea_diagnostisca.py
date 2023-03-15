from tkinter import *
from PIL import ImageTk, Image

#---------------------------------------------------
# CODIGO CREADO POR HUGO FAUNDEZ Y MIGUEL VALLADARES
#---------------------------------------------------

root = Tk()
root.title("Tarea")


chiste = ImageTk.PhotoImage(Image.open('1.jpeg'))
chiste1 = ImageTk.PhotoImage(Image.open('2.jpeg'))
chiste2 = ImageTk.PhotoImage(Image.open('3.jpeg'))
chiste3 = ImageTk.PhotoImage(Image.open('4.jpeg'))
chiste4 = ImageTk.PhotoImage(Image.open('5.jpeg'))
chiste5 = ImageTk.PhotoImage(Image.open('6.jpeg'))


lista_chistes = [chiste , chiste1 , chiste2, chiste3, chiste4, chiste5]

label = Label(root, image=chiste )
label.grid(row=0,column=0,columnspan=3)


def clase_siguiente(n_chistes):
    global label
    global anterior
    global siguiente

    label.grid_forget()
    label = Label(root,image = lista_chistes[n_chistes])
    
    anterior = Button(root, text='←', command=lambda: clase_anterior(n_chistes - 1))
    siguiente = Button(root, text='SI, quiero ver chistes', command=lambda: clase_siguiente(n_chistes + 1))

    if n_chistes == 2:
        siguiente = Button(root, text='--------------------', state=DISABLED)
    
    label.grid(row=0,column=0,columnspan=3)
    anterior.grid(row=1,column=0)
    siguiente.grid(row=1,column=2)


def clase_anterior(n_chistes):
    global label
    global anterior
    global siguiente

    label.grid_forget()
    label = Label(root,image = lista_chistes[n_chistes])
    
    anterior = Button(root, text='←', command=lambda: clase_anterior(n_chistes - 1))
    siguiente = Button(root, text='→', command=lambda: clase_siguiente(n_chistes + 1))

    if n_chistes == 0:
        anterior = Button(root, text='.', state= DISABLED)
    label.grid(row=0,column=0,columnspan=3)

    anterior.grid(row=1,column=0)
    siguiente.grid(row=1,column=2)


anterior = Button(root, text='X', state=DISABLED)
anterior.grid(row=1,column=0)

salir = Button(root, text='No quiero ver chistes', command=root.quit)
salir.grid(row=1,column=1)

siguiente = Button(root, text='SI, quiero ver chistes', command=lambda: clase_siguiente(1))
siguiente.grid(row=1,column=2)

root.mainloop()