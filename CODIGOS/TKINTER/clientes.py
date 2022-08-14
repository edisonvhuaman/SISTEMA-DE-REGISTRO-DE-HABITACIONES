import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox

#Creando la conexion
conexion = pymysql.connect(
    host = 'localhost', 
    user = 'root',
    password = 'edison',
    db = 'al3',
    port = 3334
)

print("Conexion exitosa")

#Empieza codigo tkinter
root = Tk()
root.title("Clientes")



#Variables
id_cli = StringVar()
id_habc = StringVar()
nombre = StringVar()

#Frame1
frame1=Frame(root)
frame1.pack()
    #Labels
labelId_cli = Label(frame1, text = "ID_CLIENTE ")    
labelId_cli.grid(row=1, column=1, padx=10, pady=10, sticky='e')
labelId_habc = Label(frame1, text = "ID_HAB ")    
labelId_habc.grid(row=2, column=1, padx=10, pady=10, sticky='e')
labelNombre = Label(frame1, text = "NOMBRE ")    
labelNombre.grid(row=3, column=1, padx=10, pady=10, sticky='e')
    #Cuadros
entryId_cli = Entry(frame1, textvariable=id_cli)    
entryId_cli.grid(row=1, column=2, padx=10, pady=10)
entryId_habc = Entry(frame1, textvariable=id_habc)    
entryId_habc.grid(row=2, column=2, padx=10, pady=10)
entryNombre = Entry(frame1, textvariable=nombre)    
entryNombre.grid(row=3, column=2, padx=10, pady=10)

#dando definiciones a los botones
def codCrear():
    datos_cli = id_cli.get(), id_habc.get(), nombre.get()
    #idC=id.get()
    #nomC=nombre.get()
    #edC=edad.get()
    #usuC=usuario.get()
    #conC=contraseña.get()

    curCrear=conexion.cursor()
    curCrear.execute("INSERT INTO CLIENTES VALUES {}".format(datos_cli))
    conexion.commit()
    #conexion.close()
    print("Creado exitosamente")
    limpiar()
    
    
def codLeer():
    curLeer=conexion.cursor()
    curLeer.execute("SELECT ID_CLIENTE, ID_HAB, NOMBRE FROM CLIENTES WHERE ID_CLIENTE = '{}';".format(id_cli.get()))
    for ID_CLIENTE, ID_HAB, NOMBRE in curLeer.fetchall():
        print(ID_CLIENTE, ID_HAB, NOMBRE)

        id_cli.set(ID_CLIENTE)
        id_habc.set(ID_HAB)
        nombre.set(NOMBRE)
        #conexion.close()

def codActualizar():
    datosA = [id_habc.get(), nombre.get(), id_cli.get()]
    #idA=id.get()
    #nomA=nombre.get()
    #edA=edad.get()
    #usuA=usuario.get()
    #conA=contraseña.get()

    curActualizar=conexion.cursor()
    #curActualizar.execute("UPDATE PERSONA SET NOMBRE={}, EDAD={}, USUARIO={}, CONTRASENA={} WHERE IDPERSONA={}".format(nomA, edA, usuA, conA, idA))
    curActualizar.execute("UPDATE CLIENTES SET ID_HAB=%s, NOMBRE=%s WHERE ID_CLIENTE=%s", datosA)
    conexion.commit()
    limpiar()
    #conexion.close()
    print("Actualizacion exitosa")

def codEliminar():
    curElim=conexion.cursor()
    curElim.execute("DELETE FROM CLIENTES WHERE ID_CLIENTE=%s", id_cli.get())
    conexion.commit()
    limpiar()
    print("Eliminado con exito")

#frame2 (botones)
frame2 = Frame(root)
frame2.pack()
#botones
btnCrear=Button(frame2, text="Crear", cursor="hand2", command=codCrear)
btnCrear.grid(row=1, column=1, padx=10, pady=10)
btnLeer=Button(frame2, text="Leer", cursor="hand2", command=codLeer)
btnLeer.grid(row=1, column=2, padx=10, pady=10)
btnActualizar=Button(frame2, text="Actualizar", cursor="hand2", command=codActualizar)
btnActualizar.grid(row=1, column=3, padx=10, pady=10)
btnEliminar=Button(frame2, text="Eliminar", cursor="hand2", command=codEliminar)
btnEliminar.grid(row=1, column=4, padx=10, pady=10)


#Funciones para el menu var
#limpiar
def limpiar():
    id_cli.set("")
    id_habc.set("")
    nombre.set("")
#MENSAJE
def mensaje():
    messagebox.showinfo("Acerca", """ 
    Sistema de Registro de alquileres/ Clientes
    Version 1.0
    Unsando Tkinter y mysql
    Hecho por Edison Velasco Huaman
    """)
#Salir
def salir():
    root.destroy()

#############MENU BAR#################################
menuBar=Menu(root)
#menu1=Menu(menuBar, tearoff=0)
menuBar.add_command(label="Limpiar", command=limpiar)
menuBar.add_command(label="Acerca", command=mensaje)
#menuBar.add_cascade(label="Inicio", menu=menu1)

#menu2=Menu(menuBar, tearoff=0)
#menu2.add_command(label="Salir", command=salir)
menuBar.add_command(label="Salir",command=salir)

root.config(menu=menuBar)

root.mainloop()