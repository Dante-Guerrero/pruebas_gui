
from tkinter import *

def prueba1():
    nombre = data_nombre.get()
    apellido = data_apellido.get()
    sexo = data_sexo.get()
    if sexo == 1:
        sexo = "Masculino"
    else:
        sexo = "Femenino"
    print(nombre, apellido, sexo)

root = Tk()

##########
# NOMBRE #
##########

etiqueta = Label(
    root, 
    text= "Nombre:",
    anchor="w",
    )
etiqueta.grid(row= 1, column=0, sticky='news', pady=2, padx=8)

data_nombre = StringVar()
entrada = Entry(root, textvariable=data_nombre)
entrada.grid(row=2, column=0, pady=2, padx=8)

############
# APELLIDO # 
############

etiqueta = Label(
    root, 
    text= "Apellido:",
    anchor="w",
    )
etiqueta.grid(row= 3, column=0, sticky='news', pady=2, padx=8)

data_apellido = StringVar()
entrada = Entry(root, textvariable=data_apellido)
entrada.grid(row=4, column=0, pady=2, padx=8)

#######################
# RADIOBOTONES - SEXO #
#######################

etiqueta = Label(
    root, 
    text= "Sexo:",
    anchor="w",
    )
etiqueta.grid(row= 5, column=0, sticky='news', pady=2, padx=8)

data_sexo = IntVar()
radioboton = Radiobutton(root, text= "Masculino", variable= data_sexo, value=1)
radioboton.grid(row=6, column=0, pady=2, padx=8)
radioboton2 = Radiobutton(root, text= "Femenino", variable= data_sexo, value=2)
radioboton2.grid(row=7, column=0, pady=2, padx=8)

#########
# BOTON #
#########

boton = Button(
    root, 
    text= "Da click", 
    command=prueba1,
    relief="flat",
    cursor="hand2",
    bg="#FFFF33",
    width = 10
    )
boton.grid(row= 8, column=0, pady=6, padx=8)

#############
# MAIN LOOP #
#############

root.mainloop()
