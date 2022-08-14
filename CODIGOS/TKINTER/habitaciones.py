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
root.title("Habitaciones")



#Variables
id_hab = StringVar()
precio = StringVar()
descripcion = StringVar()

#Frame1
frame1=Frame(root)
frame1.pack()
    #Labels
labelId = Label(frame1, text = "ID_HAB ")    
labelId.grid(row=1, column=1, padx=10, pady=10, sticky='e')
labelPrecio = Label(frame1, text = "PRECIO ")    
labelPrecio.grid(row=2, column=1, padx=10, pady=10, sticky='e')
labelDescripcion = Label(frame1, text = "DESCRIPCION ")    
labelDescripcion.grid(row=3, column=1, padx=10, pady=10, sticky='e')
    #Cuadros
entryId = Entry(frame1, textvariable=id_hab)    
entryId.grid(row=1, column=2, padx=10, pady=10)
entryPrecio = Entry(frame1, textvariable=precio)    
entryPrecio.grid(row=2, column=2, padx=10, pady=10)
entryDescripcion = Entry(frame1, textvariable=descripcion)    
entryDescripcion.grid(row=3, column=2, padx=10, pady=10)

#dando definiciones a los botones
def codCrear():
    datos_hab = id_hab.get(), precio.get(), descripcion.get()
    #idC=id.get()
    #nomC=nombre.get()
    #edC=edad.get()
    #usuC=usuario.get()
    #conC=contraseña.get()

    curCrear=conexion.cursor()
    curCrear.execute("INSERT INTO hab VALUES {}".format(datos_hab))
    conexion.commit()
    #conexion.close()
    print("Creado exitosamente")
    limpiar()
    
    
def codLeer():
    curLeer=conexion.cursor()
    curLeer.execute("SELECT ID_HAB, PRECIO, DESCRIPCION FROM HAB WHERE ID_HAB = '{}';".format(id_hab.get()))
    for ID_HAB, PRECIO, DESCRIPCION in curLeer.fetchall():
        print(ID_HAB, PRECIO, DESCRIPCION)

        id_hab.set(ID_HAB)
        precio.set(PRECIO)
        descripcion.set(DESCRIPCION)
        #conexion.close()

def codActualizar():
    datosA = [precio.get(), descripcion.get(), id_hab.get(),]
    #idA=id.get()
    #nomA=nombre.get()
    #edA=edad.get()
    #usuA=usuario.get()
    #conA=contraseña.get()

    curActualizar=conexion.cursor()
    #curActualizar.execute("UPDATE PERSONA SET NOMBRE={}, EDAD={}, USUARIO={}, CONTRASENA={} WHERE IDPERSONA={}".format(nomA, edA, usuA, conA, idA))
    curActualizar.execute("UPDATE HAB SET PRECIO=%s, DESCRIPCION=%s WHERE ID_HAB=%s", datosA)
    conexion.commit()
    limpiar()
    #conexion.close()
    print("Actualizacion exitosa")

def codEliminar():
    curElim=conexion.cursor()
    curElim.execute("DELETE FROM HAB WHERE ID_HAB=%s", id_hab.get())
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
    id_hab.set("")
    precio.set("")
    descripcion.set("")
#MENSAJE
def mensaje():
    messagebox.showinfo("Acerca", """ 
    Sistema de Registro de alquileres/ Habitaciones
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